# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import openai_pb2 as openai__pb2
import result_pb2 as result__pb2


class OpenAIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_models = channel.unary_unary(
                '/openai.OpenAI/get_models',
                request_serializer=openai__pb2.ModelRequest.SerializeToString,
                response_deserializer=result__pb2.Response.FromString,
                )
        self.chat = channel.unary_unary(
                '/openai.OpenAI/chat',
                request_serializer=openai__pb2.ChatRequest.SerializeToString,
                response_deserializer=result__pb2.Response.FromString,
                )


class OpenAIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_models(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def chat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OpenAIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_models': grpc.unary_unary_rpc_method_handler(
                    servicer.get_models,
                    request_deserializer=openai__pb2.ModelRequest.FromString,
                    response_serializer=result__pb2.Response.SerializeToString,
            ),
            'chat': grpc.unary_unary_rpc_method_handler(
                    servicer.chat,
                    request_deserializer=openai__pb2.ChatRequest.FromString,
                    response_serializer=result__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'openai.OpenAI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OpenAI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_models(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/openai.OpenAI/get_models',
            openai__pb2.ModelRequest.SerializeToString,
            result__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def chat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/openai.OpenAI/chat',
            openai__pb2.ChatRequest.SerializeToString,
            result__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)