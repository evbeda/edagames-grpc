import pytest
from unittest.mock import AsyncMock

from edagames_grpc.client import ClientGRPC

import edagames_grpc.eda_games_pb2 as eda_games_pb2


@pytest.fixture
def test_client():
    client = ClientGRPC('127.0.0.1', 50051)
    client.stub = AsyncMock()

    # GameStart mock object
    game_start_mock = eda_games_pb2.GameStartResponse()
    game_start_mock.idgame = '0001'
    game_start_mock.current_player = 'Player 1'
    game_start_mock.turn_data.update({})

    # GameState mock object
    game_state_mock = eda_games_pb2.GameStateResponse()
    game_state_mock.game_id = 'Player 1'
    game_state_mock.current_player = 'Player 2'
    game_state_mock.turn_data.update({})
    game_state_mock.play_data.update({})

    client.stub.CreateGame.return_value = game_start_mock
    client.stub.ExecuteAction.return_value = game_state_mock
    client.stub.EndGame.return_value = game_state_mock
    client.stub.Penalize.return_value = game_state_mock

    return client


@pytest.mark.asyncio
async def test_client_create_game(test_client):
    await test_client.create_game(['Player 1', 'Player 2'])
    test_client.stub.CreateGame.assert_called()


@pytest.mark.asyncio
async def test_client_execute_action(test_client):
    await test_client.execute_action(
        '0001',
        {},
    )
    test_client.stub.ExecuteAction.assert_called()


@pytest.mark.asyncio
async def test_client_end_game(test_client):
    await test_client.end_game('0001')
    test_client.stub.EndGame.assert_called()


@pytest.mark.asyncio
async def test_client_penalize(test_client):
    await test_client.penalize('0001')
    test_client.stub.Penalize.assert_called()
