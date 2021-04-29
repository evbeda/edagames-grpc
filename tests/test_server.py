from unittest.mock import AsyncMock
import pytest

from edagames_grpc.game_start import GameStart
from edagames_grpc.game_state import GameState
from edagames_grpc.utils import struct_to_dict

from edagames_grpc.server import ServerGRPC
from edagames_grpc.server import ServerInterface
from edagames_grpc import eda_games_pb2
from edagames_grpc import eda_games_pb2_grpc


# Test Server Interface
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
async def test_server_start_and_wait(server_interface):
    server_patched = AsyncMock()
    server_interface.server = server_patched
    await server_interface.start_and_wait()
    server_patched.start.assert_called()
    server_patched.wait_for_termination.assert_called()


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
    delegate.create_game.return_value = GameStart(
        '0001',
        'Player 1',
        {'data': 'turn_data'},
    )
    example_game_state = GameState(
        'Player 1',
        'Player 2',
        {'data': 'turn_data'},
        {'data': 'play_data'},
    )
    delegate.execute_action.return_value = example_game_state
    delegate.end_game.return_value = example_game_state
    delegate.penalize.return_value = example_game_state
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
    assert struct_to_dict(response.turn_data) == {'data': 'turn_data'}


@pytest.mark.asyncio
async def test_execute_action(grpc_stub):
    request = eda_games_pb2.ExecuteActionRequest()
    request.idgame = '0001'
    request.data.update({
        'action': 'move',
        'data': {
            'from_row': 1,
            'to_row': 2,
        },
    })
    response = await grpc_stub.ExecuteAction(request)
    assert response.previous_player == 'Player 1'
    assert response.current_player == 'Player 2'
    assert struct_to_dict(response.turn_data) == {'data': 'turn_data'}
    assert struct_to_dict(response.play_data) == {'data': 'play_data'}


@pytest.mark.asyncio
async def test_end_game(grpc_stub):
    request = eda_games_pb2.Idgame(idgame='0001')
    response = await grpc_stub.EndGame(request)
    assert response.previous_player == 'Player 1'
    assert response.current_player == 'Player 2'
    assert struct_to_dict(response.turn_data) == {'data': 'turn_data'}
    assert struct_to_dict(response.play_data) == {'data': 'play_data'}


@pytest.mark.asyncio
async def test_penalize(grpc_stub):
    request = eda_games_pb2.Idgame(idgame='0001')
    response = await grpc_stub.Penalize(request)
    assert response.previous_player == 'Player 1'
    assert response.current_player == 'Player 2'
    assert struct_to_dict(response.turn_data) == {'data': 'turn_data'}
    assert struct_to_dict(response.play_data) == {'data': 'play_data'}
