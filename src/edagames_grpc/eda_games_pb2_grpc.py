# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import eda_games_pb2 as eda__games__pb2


class EdaGameServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGame = channel.unary_unary(
                '/EdaGameService/CreateGame',
                request_serializer=eda__games__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=eda__games__pb2.GameStartResponse.FromString,
                )
        self.ExecuteAction = channel.unary_unary(
                '/EdaGameService/ExecuteAction',
                request_serializer=eda__games__pb2.ExecuteActionRequest.SerializeToString,
                response_deserializer=eda__games__pb2.GameStateResponse.FromString,
                )
        self.EndGame = channel.unary_unary(
                '/EdaGameService/EndGame',
                request_serializer=eda__games__pb2.Idgame.SerializeToString,
                response_deserializer=eda__games__pb2.GameStateResponse.FromString,
                )
        self.Penalize = channel.unary_unary(
                '/EdaGameService/Penalize',
                request_serializer=eda__games__pb2.Idgame.SerializeToString,
                response_deserializer=eda__games__pb2.GameStateResponse.FromString,
                )


class EdaGameServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Penalize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EdaGameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGame': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGame,
                    request_deserializer=eda__games__pb2.CreateGameRequest.FromString,
                    response_serializer=eda__games__pb2.GameStartResponse.SerializeToString,
            ),
            'ExecuteAction': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteAction,
                    request_deserializer=eda__games__pb2.ExecuteActionRequest.FromString,
                    response_serializer=eda__games__pb2.GameStateResponse.SerializeToString,
            ),
            'EndGame': grpc.unary_unary_rpc_method_handler(
                    servicer.EndGame,
                    request_deserializer=eda__games__pb2.Idgame.FromString,
                    response_serializer=eda__games__pb2.GameStateResponse.SerializeToString,
            ),
            'Penalize': grpc.unary_unary_rpc_method_handler(
                    servicer.Penalize,
                    request_deserializer=eda__games__pb2.Idgame.FromString,
                    response_serializer=eda__games__pb2.GameStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EdaGameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EdaGameService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdaGameService/CreateGame',
            eda__games__pb2.CreateGameRequest.SerializeToString,
            eda__games__pb2.GameStartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdaGameService/ExecuteAction',
            eda__games__pb2.ExecuteActionRequest.SerializeToString,
            eda__games__pb2.GameStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdaGameService/EndGame',
            eda__games__pb2.Idgame.SerializeToString,
            eda__games__pb2.GameStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Penalize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EdaGameService/Penalize',
            eda__games__pb2.Idgame.SerializeToString,
            eda__games__pb2.GameStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
