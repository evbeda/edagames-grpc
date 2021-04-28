import grpc
from typing import Dict, List

from .game_state import GameState
from .game_start import GameStart
from .utils import struct_to_dict

from edagames_grpc import eda_games_pb2
from edagames_grpc import eda_games_pb2_grpc


class ServerGRPC(eda_games_pb2_grpc.EdaGameServiceServicer):

    def __init__(self, delegate: 'ServerInterface'):
        super().__init__()
        self.delegate = delegate

    async def CreateGame(
        self,
        request: eda_games_pb2.CreateGameRequest,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStartResponse:
        game_start = await self.delegate.create_game(
            request.players,
        )
        return game_start.to_protobuf_struct()

    async def ExecuteAction(
        self,
        request: eda_games_pb2.ExecuteActionRequest,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:
        game_state = await self.delegate.execute_action(
            request.idgame,
            struct_to_dict(request.data),
        )
        return game_state.to_protobuf_struct()

    async def EndGame(
        self,
        request: eda_games_pb2.Idgame,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:
        game_state = await self.delegate.end_game(
            request.idgame,
        )
        return game_state.to_protobuf_struct()

    async def Penalize(
        self,
        request: eda_games_pb2.Idgame,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:
        game_state = await self.delegate.penalize(
            request.idgame,
        )
        return game_state.to_protobuf_struct()


class ServerInterface:

    def __init__(self, bind_ip: str = '0.0.0.0', port: int = 50001):
        listen_addr = f'{bind_ip}:{port}'
        self.server = grpc.aio.server()
        eda_games_pb2_grpc.add_EdaGameServiceServicer_to_server(
            ServerGRPC(self),
            self.server,
        )
        self.server.add_insecure_port(listen_addr)

    async def start(self):
        return await self.server.start()

    async def stop(self, timeout=0):
        return await self.server.stop(timeout)

    async def start_and_wait(self):
        await self.start()
        await self.server.wait_for_termination()

    async def create_game(self, players: List[str]) -> GameStart:
        raise NotImplementedError

    async def execute_action(self, game_id: str, game_data: Dict) -> GameState:
        raise NotImplementedError

    async def end_game(self, game_id: str) -> GameState:
        raise NotImplementedError

    async def penalize(self, game_id: str) -> GameState:
        raise NotImplementedError
