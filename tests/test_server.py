import unittest
from unittest.mock import patch, AsyncMock
from edagames_grpc.server import ServerGRPC
from edagames_grpc.server import ServerInterface
import grpc_testing


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
        servicer = _server_application.FirstServiceServicer()
        descriptors_to_servicers = {
            _application_testing_common.FIRST_SERVICE: servicer
        }
        self._real_time_server = grpc_testing.server_from_dictionary(
            descriptors_to_servicers, self._real_time)