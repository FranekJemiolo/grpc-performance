import asyncio
import json
import logging

import click
from grpclib.client import Channel
from tqdm import tqdm

import grpc_performance.grpc_performance_pb2
from grpc_performance.grpc_performance_grpc import DataStreamerStub


async def run(batch_mode, num_messages):
    async with Channel('localhost', 50051) as channel:
        data_streamer = DataStreamerStub(channel)
        pbar = tqdm(total=num_messages)
        try:
            if not batch_mode:
                async with data_streamer.streamData.open() as stream:
                    await stream.send_message(grpc_performance.grpc_performance_pb2.StreamRequest(
                        jsonRequest=json.dumps({"num_messages": num_messages}).encode('ascii')))
                    async for msg in stream:
                        pbar.update(1)
            else:
                async with data_streamer.streamBatchData.open() as stream:
                    await stream.send_message(grpc_performance.grpc_performance_pb2.StreamRequest(
                        jsonRequest=json.dumps({"num_messages": num_messages}).encode('ascii')))
                    async for msgs in stream:
                        for msg in msgs.messages:
                            pbar.update(1)
        finally:
            pbar.close()


@click.command()
@click.option("--batch-mode",
              help="Run in batch mode",
              is_flag=True)
@click.option("--num-messages",
              help="Number of messages on which you want to test the client",
              default=1000000)
def main(batch_mode, num_messages):
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run(batch_mode, num_messages))


if __name__ == '__main__':
    main()
