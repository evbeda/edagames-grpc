import pytest
from unittest.mock import AsyncMock

from edagames_grpc.client import ClientGRPC


@pytest.fixture
def test_client():
    client = ClientGRPC('127.0.0.1', 50051)
    client.stub = AsyncMock()
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
