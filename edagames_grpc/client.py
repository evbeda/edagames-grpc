import grpc
import eda_games_pb2
import eda_games_pb2_grpc
from google.protobuf.struct_pb2 import Struct


class ClientGRPC:
    def __init__(self):
        self.stub = self.start()

    def start(self):
        channel = grpc.insecure_channel('localhost:50051')
        stub = eda_games_pb2_grpc.EdaGameServiceStub(channel)
        return stub

    async def CreateGame(self, players):
        return self.stub.CreateGame(
            eda_games_pb2.CreateGameRequest(players=players)
        )

    async def ExecuteAction(self, id, data_dict):
        data_struct = Struct()
        data_struct.update(data_dict)
        return self.stub.ExecuteAction(
            eda_games_pb2.ExecuteActionRequest(idgame=id, data=data_struct)
        )

    async def EndGame(self, id):
        return self.stub.EndGame(
            eda_games_pb2.Idgame(idgame=id)
        )

    async def Penalize(self, id):
        return self.stub.Penalize(
            eda_games_pb2.Idgame(idgame=id)
        )
