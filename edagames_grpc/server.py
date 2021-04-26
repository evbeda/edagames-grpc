import grpc
import eda_games_pb2
import eda_games_pb2_grpc


class EdaGamesService(eda_games_pb2_grpc.EdaGameServiceServicer):
    pass


class EdaGamesGRPC:
    def __init__(self, bind_ip: str = '0.0.0.0', port: int = 50001):
        listen_addr = f'{bind_ip}:{port}'
        self.server = grpc.aio.server()
        eda_games_pb2_grpc.add_EdaGameServiceServicer_to_server(
            EdaGamesService(),
            self.server,
        )
        self.server.add_insecure_port(listen_addr)

    async def start(self):
        return await self.server.start()

    async def stop(self, timeout=0):
        return await self.server.stop(timeout)
