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

    async def Saludo(self):
        response = self.stub.SayHello(
            eda_games_pb2.HelloRequest(name='you')
        )
        return "Greeter client received: {}".format(response.message)

    async def CreateGame(self, players):
        response = self.stub.CreateGame(
            eda_games_pb2.CreateGameRequest(players=players)
        )
        return "Echo the list of players: {}".format(response.idgame)

    async def ExecuteAction(self, id):
        response = self.stub.ExecuteAction(
            eda_games_pb2.ExecuteActionRequest(idgame=id)
        )
        return "Echo execute action: {}".format(response.next_player)

    async def EndGame(self, id):
        response = self.stub.EndGame(
            eda_games_pb2.Idgame(idgame=id)
        )
        return "Echo endgame: {}".format(response.next_player)

    async def Penalize(self, id):
        response = self.stub.Penalize(
            eda_games_pb2.Idgame(idgame=id)
        )
        return "Echo penalize: {}".format(response.next_player)


async def testing():
    x = ClientGRPC()
    print(await x.Saludo())
    print(await x.CreateGame(['Juan', 'Marcos']))
    print(await x.ExecuteAction('123'))
    print(await x.EndGame('123'))
    print(await x.Penalize('123'))


asyncio.run(testing())
