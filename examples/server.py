import asyncio

from edagames_grpc.server import ServerInterface
from edagames_grpc.game_state import GameState
from edagames_grpc.game_start import GameStart


class TestGame:
    def __init__(self, players):
        self.players = players
        self.current = 0
        self.prev = None
        TestGame.instance = self


class ServerTest(ServerInterface):

    async def create_game(self, players):
        print(f'Received players: {players}')

        TestGame(players)
        gid = '0000-0001'
        print(f'Returned game id: {gid}')
        return GameStart(gid, 'uno', {})

    async def execute_action(self, game_id, game_data):
        print(f'Received game id: {game_id}')
        print(f'Received game data: {game_data}')

        TestGame.instance.prev = TestGame.instance.current
        TestGame.instance.current = (TestGame.instance.current + 1) % 2

        game_data.update({'state': 'valid'})

        game_state = GameState(
            f'Player {TestGame.instance.current + 1}',
            f'Player {TestGame.instance.prev + 1}',
            {'board': 'xxxxxxxxxxxxxxxxxxx'},
            {'action': 'move', 'data': game_data},
        )
        print(f'Returned game state: {game_state}')
        return game_state


if __name__ == '__main__':
    s = ServerTest(port=50051)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.start_and_wait())
    loop.run_forever()
