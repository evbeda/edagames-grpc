import unittest
from unittest.mock import patch, AsyncMock
from edagames_grpc.server import EdaGamesGRPC


class TestGRPCServer(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.server = EdaGamesGRPC()

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
