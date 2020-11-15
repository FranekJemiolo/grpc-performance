import asyncio
import json
import logging

import grpc
from tqdm import tqdm

import grpc_performance.grpc_performance_pb2
import grpc_performance.grpc_performance_pb2_grpc


async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = grpc_performance.grpc_performance_pb2_grpc.DataStreamerStub(channel)
        num_messages = 100000
        pbar = tqdm(total=num_messages)
        try:
            async for msg in stub.streamData(grpc_performance.grpc_performance_pb2.StreamRequest(
                    jsonRequest=json.dumps({"num_messages": num_messages}).encode('ascii'))):
                pbar.update(1)
        finally:
            pbar.close()


def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run())


if __name__ == '__main__':
    main()
