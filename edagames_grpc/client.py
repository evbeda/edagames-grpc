import grpc
import eda_games_pb2
import eda_games_pb2_grpc
from google.protobuf.struct_pb2 import Struct


class ClientGRPC:
    def __init__(self):
        channel = grpc.aio.insecure_channel('localhost:50051')
        self.stub = eda_games_pb2_grpc.EdaGameServiceStub(channel)

    async def create_game(self, players):
        request = eda_games_pb2.CreateGameRequest(players=players)
        return await self.stub.CreateGame(request)

    async def execute_action(self, game_id, data_dict):
        data_struct = Struct()
        data_struct.update(data_dict)
        request = eda_games_pb2.ExecuteActionRequest(idgame=game_id, data=data_struct)
        return await self.stub.ExecuteAction(request)

    async def end_game(self, game_id):
        return await self.stub.EndGame(
            eda_games_pb2.Idgame(idgame=game_id)
        )

    async def penalize(self, game_id):
        return await self.stub.Penalize(
            eda_games_pb2.Idgame(idgame=game_id)
        )
