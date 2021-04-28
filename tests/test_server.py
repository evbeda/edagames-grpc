import grpc_testing
import unittest
from unittest.mock import AsyncMock

from src.edagames_grpc.server import ServerGRPC
from src.edagames_grpc.server import ServerInterface
from src.edagames_grpc import eda_games_pb2


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
