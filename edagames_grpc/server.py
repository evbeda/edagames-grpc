import grpc
import eda_games_pb2
import eda_games_pb2_grpc
from game_state import GameState
from typing import Dict


class EdaGamesService(eda_games_pb2_grpc.EdaGameServiceServicer):
    def __init__(self, delegate):
        super().__init__()
        self.delegate = delegate

    async def CreateGame(
        self,
        request: eda_games_pb2.CreateGameRequest,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.Idgame:
        game_id = self.delegate.create_game(request.players)
        return eda_games_pb2.Idgame(idgame=game_id)

    async def ExecuteAction(
        self,
        request: eda_games_pb2.Idgame,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:
        game_state = self.delegate.execute_action(
            request.idgame,
            request.data,
        )
        response = eda_games_pb2.GameStateResponse()
        response.current_player = game_state.current_player
        response.next_player = game_state.next_player
        response.turn_data.update(game_state.turn_data)
        response.play_data.update(game_state.play_data)
        return response

    async def EndGame(
        self,
        request: eda_games_pb2.Idgame,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:


    async def Penalize(
        self,
        request: eda_games_pb2.Idgame,
        context: grpc.aio.ServicerContext,
    ) -> eda_games_pb2.GameStateResponse:
        pass


class EdaGamesGRPC:
    def __init__(self, bind_ip: str = '0.0.0.0', port: int = 50001):
        listen_addr = f'{bind_ip}:{port}'
        self.server = grpc.aio.server()
        eda_games_pb2_grpc.add_EdaGameServiceServicer_to_server(
            EdaGamesService(self),
            self.server,
        )
        self.server.add_insecure_port(listen_addr)

    async def start(self):
        return await self.server.start()

    async def stop(self, timeout=0):
        return await self.server.stop(timeout)

    async def create_game(players: list[str]) -> str:
        raise NotImplementedError

    async def execute_action(game_id: str, game_data: Dict[]) -> GameState:
        raise NotImplementedError

    async def end_game(game_id: str) -> GameState:
        raise NotImplementedError

    async def penalize(game_id: str) -> GameState:
        raise NotImplementedError
