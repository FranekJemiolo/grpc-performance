import asyncio
import json
import logging

import grpc
import numpy as np

import grpc_performance.grpc_performance_pb2
import grpc_performance.grpc_performance_pb2_grpc


def get_random_messages(message_size, batch_size):
    np.random.seed(42)
    return [np.random.bytes(message_size) for i in range(batch_size)]


class DataStreamer(grpc_performance.grpc_performance_pb2_grpc.DataStreamerServicer):

    async def streamData(self, request, context):
        data = json.loads(request.jsonRequest)
        random_messages = get_random_messages(100, 1)
        random_message = random_messages[0]
        for i in range(data['num_messages']):
            yield grpc_performance.grpc_performance_pb2.SingleMessage(message=random_message)


async def serve():
    server = grpc.aio.server()
    grpc_performance.grpc_performance_pb2_grpc.add_DataStreamerServicer_to_server(DataStreamer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info(f"starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()


def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())


if __name__ == "__main__":
    main()
