import asyncio
import json
import logging
import math
import random

import click
import grpc
import numpy as np

import grpc_performance.grpc_performance_pb2
import grpc_performance.grpc_performance_pb2_grpc


compression_algos = {
    'NoCompression': grpc.Compression.NoCompression,
    'Deflate': grpc.Compression.Deflate,
    'Gzip': grpc.Compression.Gzip
}


def get_random_messages(message_size, batch_size):
    np.random.seed(42)
    return [np.random.bytes(message_size) for i in range(batch_size)]


class DataStreamer(grpc_performance.grpc_performance_pb2_grpc.DataStreamerServicer):
    def __init__(self, batch_size, compression):
        super().__init__()
        self.batch_size = batch_size
        self.compression = compression

    async def streamData(self, request, context):
        data = json.loads(request.jsonRequest)
        random_messages = get_random_messages(100, 1)
        random_message = random_messages[0]
        for i in range(data['num_messages']):
            yield grpc_performance.grpc_performance_pb2.SingleMessage(message=random_message)

    async def streamBatchData(self, request, context):
        data = json.loads(request.jsonRequest)
        random_messages = get_random_messages(100, self.batch_size)
        batch = []
        num_messages = data['num_messages']
        for i in range(num_messages):
            random_message = random_messages[random.randrange(0, self.batch_size)]
            batch.append(grpc_performance.grpc_performance_pb2.SingleMessage(message=random_message))
            if len(batch) >= self.batch_size:
                yield grpc_performance.grpc_performance_pb2.BatchMessage(messages=batch)
                batch = []
        if len(batch) > 0:
            yield grpc_performance.grpc_performance_pb2.BatchMessage(messages=batch)


async def serve(batch_size, compression):
    server = grpc.aio.server()
    grpc_performance.grpc_performance_pb2_grpc.add_DataStreamerServicer_to_server(
        DataStreamer(batch_size, compression), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info(f"starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()


@click.command()
@click.option("--batch-size",
              help="Set the number of messages sent in one request",
              default=1)
@click.option("--compression",
              help="Choose the type of compression for the message",
              type=click.Choice(["NoCompression", "Gzip", "Deflate"], case_sensitive=False),
              default="NoCompression")
def main(batch_size, compression):
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(batch_size, compression))


if __name__ == "__main__":
    main()
