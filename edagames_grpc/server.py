import grpc
import edagames_pb2
import edagames_pb2_grpc


class EdaGamesService(edagames_pb2_grpc.TestServiceServicer):
    pass


class EdaGamesGRPC:
    def __init__(self, bind_ip: str = '0.0.0.0', port: int = 50001):
        listen_addr = f'{bind_ip}:{port}'
        self.server = grpc.aio.server()
        edagames_pb2_grpc.add_EdaGamesServiceServicer_to_server(
            EdaGamesService(),
            self.server
        )
        self.server.add_insecure_port(listen_addr)

    async def start(self):
        return await self.server.start()

    async def stop(self, timeout=0):
        return await self.server.stop(timeout)
