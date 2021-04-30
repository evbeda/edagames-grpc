import grpc
from google.protobuf.struct_pb2 import Struct

from edagames_grpc.game_state import GameState
from edagames_grpc.game_start import GameStart

from edagames_grpc import eda_games_pb2
from edagames_grpc import eda_games_pb2_grpc


class ClientGRPC:
    def __init__(self, server_ip: str = '0.0.0.0', port: int = 50001):
        channel = grpc.aio.insecure_channel(f'{server_ip}:{port}')
        self.stub = eda_games_pb2_grpc.EdaGameServiceStub(channel)

    async def create_game(self, players):
        response = await self.stub.CreateGame(
            eda_games_pb2.CreateGameRequest(players=players)
        )
        return GameStart.from_protobuf_game_start_response(response)

    async def execute_action(self, game_id, data_dict):
        data_struct = Struct()
        data_struct.update(data_dict)
        response = await self.stub.ExecuteAction(
            eda_games_pb2.ExecuteActionRequest(
                idgame=game_id,
                data=data_struct,
            )
        )
        return GameState.from_protobuf_game_state_response(response)

    async def end_game(self, game_id):
        response = await self.stub.EndGame(
            eda_games_pb2.Idgame(idgame=game_id)
        )
        return GameState.from_protobuf_game_state_response(response)

    async def penalize(self, game_id):
        response = await self.stub.Penalize(
            eda_games_pb2.Idgame(idgame=game_id)
        )
        return GameState.from_protobuf_game_state_response(response)
