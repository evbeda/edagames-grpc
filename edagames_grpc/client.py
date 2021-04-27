import grpc
import asyncio
import eda_games_pb2
import eda_games_pb2_grpc


class ClientGRPC:
    def __init__(self):
        self.stub = self.start()

    def start(self):
        channel = grpc.insecure_channel('localhost:50051')
        stub = eda_games_pb2_grpc.EdaGameServiceStub(channel)
        return stub

    async def CreateGame(self, players):
        response = self.stub.CreateGame(
            eda_games_pb2.CreateGameRequest(players=players)
        )
        return "Echo the list of players: " + response.idgame


class ClientInterface:
    def __init__(self):
        self.grpc = ClientGRPC()

    async def create_game(self, players):
        if type(players) == list:
            return await self.grpc.CreateGame(players)
        else:
            return 'Pasame una list'


async def testing():
    x = ClientInterface()
    print(await x.create_game(['Juan', 'Marcos']))


asyncio.run(testing())
