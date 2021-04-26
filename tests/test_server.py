import unittest
from unittest.mock import patch, AsyncMock
from edagames_grpc.server import EdaGamesGRPC


class TestGRPCServer(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.server = EdaGamesGRPC()

    async def test_start(self):
        with patch.object(EdaGamesGRPC, 'server', new_callable=AsyncMock) as server_patched:
            self.server.start()
        server_patched.start.assert_called()
