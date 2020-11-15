# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_performance_pb2 as grpc__performance__pb2


class DataStreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.streamData = channel.unary_stream(
                '/grpc_performance.DataStreamer/streamData',
                request_serializer=grpc__performance__pb2.StreamRequest.SerializeToString,
                response_deserializer=grpc__performance__pb2.SingleMessage.FromString,
                )
        self.streamBatchData = channel.unary_stream(
                '/grpc_performance.DataStreamer/streamBatchData',
                request_serializer=grpc__performance__pb2.StreamRequest.SerializeToString,
                response_deserializer=grpc__performance__pb2.BatchMessage.FromString,
                )


class DataStreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def streamData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def streamBatchData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataStreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'streamData': grpc.unary_stream_rpc_method_handler(
                    servicer.streamData,
                    request_deserializer=grpc__performance__pb2.StreamRequest.FromString,
                    response_serializer=grpc__performance__pb2.SingleMessage.SerializeToString,
            ),
            'streamBatchData': grpc.unary_stream_rpc_method_handler(
                    servicer.streamBatchData,
                    request_deserializer=grpc__performance__pb2.StreamRequest.FromString,
                    response_serializer=grpc__performance__pb2.BatchMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_performance.DataStreamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataStreamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def streamData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc_performance.DataStreamer/streamData',
            grpc__performance__pb2.StreamRequest.SerializeToString,
            grpc__performance__pb2.SingleMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def streamBatchData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc_performance.DataStreamer/streamBatchData',
            grpc__performance__pb2.StreamRequest.SerializeToString,
            grpc__performance__pb2.BatchMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
