from unittest.mock import AsyncMock
import pytest

from edagames_grpc.game_start import GameStart
from edagames_grpc.utils import struct_to_dict

from edagames_grpc.server import ServerGRPC
from edagames_grpc.server import ServerInterface
from edagames_grpc import eda_games_pb2
from edagames_grpc import eda_games_pb2_grpc


# Test Server Interface
@pytest.fixture
def server_interface():
    return ServerInterface()


@pytest.mark.asyncio
async def test_server_start(server_interface):
    server_patched = AsyncMock()
    server_interface.server = server_patched
    await server_interface.start()
    server_patched.start.assert_called()


@pytest.mark.asyncio
async def test_server_stop(server_interface):
    server_patched = AsyncMock()
    server_interface.server = server_patched
    await server_interface.stop()
    server_patched.stop.assert_called()


# Test gRPC
@pytest.fixture(scope='module')
def grpc_add_to_server():
    return eda_games_pb2_grpc.add_EdaGameServiceServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    delegate = AsyncMock()
    delegate.create_game.return_value = GameStart('0001', 'Player 1', {})
    return ServerGRPC(delegate)


@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    return eda_games_pb2_grpc.EdaGameServiceStub


@pytest.mark.asyncio
async def test_create_game(grpc_stub):
    request = eda_games_pb2.CreateGameRequest()
    request.players.extend(['Player 1', 'Player 2'])
    response = await grpc_stub.CreateGame(request)
    assert response.idgame == '0001'
    assert response.current_player == 'Player 1'
    assert struct_to_dict(response.turn_data) == {}
