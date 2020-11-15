import asyncio
import json
import logging

import click
import grpc
from tqdm import tqdm

import grpc_performance.grpc_performance_pb2
import grpc_performance.grpc_performance_pb2_grpc


compression_algos = {
    'NoCompression': grpc.Compression.NoCompression,
    'Deflate': grpc.Compression.Deflate,
    'Gzip': grpc.Compression.Gzip
}


async def run(batch_mode, compression, num_messages):
    async with grpc.aio.insecure_channel('localhost:50051', compression=compression_algos[compression]) as channel:
        stub = grpc_performance.grpc_performance_pb2_grpc.DataStreamerStub(channel)
        pbar = tqdm(total=num_messages)
        try:
            if not batch_mode:
                async for msg in stub.streamData(grpc_performance.grpc_performance_pb2.StreamRequest(
                        jsonRequest=json.dumps({"num_messages": num_messages}).encode('ascii'))):
                    pbar.update(1)
            else:
                async for msgs in stub.streamBatchData(grpc_performance.grpc_performance_pb2.StreamRequest(
                        jsonRequest=json.dumps({"num_messages": num_messages}).encode('ascii'))):
                    for msg in msgs.messages:
                        pbar.update(1)
        finally:
            pbar.close()


@click.command()
@click.option("--batch-mode",
              help="Run in batch mode",
              is_flag=True)
@click.option("--compression",
              help="Choose the type of compression for the message",
              type=click.Choice(["NoCompression", "Gzip", "Deflate"], case_sensitive=False),
              default="NoCompression")
@click.option("--num-messages",
              help="Number of messages on which you want to test the client",
              default=1000000)
def main(batch_mode, compression, num_messages):
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run(batch_mode, compression, num_messages))


if __name__ == '__main__':
    main()
