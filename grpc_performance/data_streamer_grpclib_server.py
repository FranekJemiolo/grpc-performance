import asyncio
import json
import logging
import random

import click
import numpy as np
from grpclib.utils import graceful_exit
from grpclib.server import Server

import grpc_performance.grpc_performance_pb2
import grpc_performance.grpc_performance_grpc


def get_random_messages(message_size, batch_size):
    np.random.seed(42)
    return [np.random.bytes(message_size) for i in range(batch_size)]


class DataStreamer(grpc_performance.grpc_performance_grpc.DataStreamerBase):
    def __init__(self, batch_size):
        super().__init__()
        self.batch_size = batch_size

    async def streamData(self, stream):
        msg = await stream.recv_message()
        data = json.loads(msg.jsonRequest)
        random_messages = get_random_messages(100, 1)
        random_message = random_messages[0]
        for i in range(data['num_messages']):
            await stream.send_message(grpc_performance.grpc_performance_pb2.SingleMessage(message=random_message))

    async def streamBatchData(self, stream):
        msg = await stream.recv_message()
        data = json.loads(msg.jsonRequest)
        random_messages = get_random_messages(100, self.batch_size)
        batch = []
        num_messages = data['num_messages']
        for i in range(num_messages):
            random_message = random_messages[random.randrange(0, self.batch_size)]
            batch.append(grpc_performance.grpc_performance_pb2.SingleMessage(message=random_message))
            if len(batch) >= self.batch_size:
                await stream.send_message(grpc_performance.grpc_performance_pb2.BatchMessage(messages=batch))
                batch = []
        if len(batch) > 0:
            await stream.send_message(grpc_performance.grpc_performance_pb2.BatchMessage(messages=batch))


async def serve(batch_size):
    server = Server([DataStreamer(batch_size)])
    with graceful_exit([server]):
        await server.start("0.0.0.0", 50051)
        logging.info(f"starting server on 0.0.0.0:50051")
        await server.wait_closed()


@click.command()
@click.option("--batch-size",
              help="Set the number of messages sent in one request",
              default=1)
def main(batch_size):
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(batch_size))


if __name__ == "__main__":
    main()
