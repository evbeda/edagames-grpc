import asyncio

from edagames_grpc.server import ServerInterface
from edagames_grpc.game_state import GameState


class ServerTest(ServerInterface):

    async def create_game(self, players):
        print(f'Received players: {players}')

        gid = '0000-0001'
        print(f'Returned game id: {gid}')
        return gid

    async def execute_action(self, game_id, game_data):
        print(f'Received game id: {game_id}')
        print(f'Received game data: {game_data}')

        game_state = GameState(
            'Player 1',
            'Player 2',
            {'board': 'xxxxxxxxxxxxxxxxxxx'},
            {'action': 'move', 'data': {'row_from': 2, 'row_to': 3}},
        )
        print(f'Returned game state: {game_state}')
        return game_state


if __name__ == '__main__':
    s = ServerTest(port=50051)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.start_and_wait())
    loop.run_forever()
