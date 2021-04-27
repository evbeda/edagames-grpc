import unittest
from unittest.mock import patch, AsyncMock
from edagames_grpc.server import ServerGRPC
from edagames_grpc.server import ServerInterface
import grpc_testing
import grpc
import eda_games_pb2


class TestServerInterface(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.server = ServerInterface()

    async def test_start(self):
        server_patched = AsyncMock()
        self.server.server = server_patched
        await self.server.start()
        server_patched.start.assert_called()

    async def test_stop(self):
        server_patched = AsyncMock()
        self.server.server = server_patched
        await self.server.stop()
        server_patched.stop.assert_called()


class TestServerGRPC(unittest.IsolatedAsyncioTestCase):

    # def setUp(self):
    #     grpc_patched = AsyncMock()
    #     self.service = EdaGamesService(grpc_patched)

    # async def test_create_game(self):
    #     pass

    def setUp(self):
        self._real_time = grpc_testing.strict_real_time()
        self.delegate = AsyncMock()
        servicer = ServerGRPC(self.delegate)
        self.service = eda_games_pb2.DESCRIPTOR.services_by_name['EdaGameService']
        descriptors_to_servicers = {
            self.service: servicer,
        }
        self.server = grpc_testing.server_from_dictionary(
            descriptors_to_servicers, self._real_time,
        )

    async def test_create_game(self):
        request = eda_games_pb2.CreateGameRequest()
        request.players.extend(['Player 1', 'Player 2'])
        self.delegate.create_game.return_value = '0001'
        rpc = self.server.invoke_unary_unary(
            self.service.methods_by_name['CreateGame'],
            (),
            request,
            None,
        )
        response, trailing_metadata, code, details = rpc.termination()
        response_awaited = await response
        expected = eda_games_pb2.Idgame(idgame='0001')
        self.assertEqual(response_awaited, expected)
        self.assertIs(code, grpc.StatusCode.OK)
