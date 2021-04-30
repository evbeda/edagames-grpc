import asyncio
from edagames_grpc.client import ClientGRPC


async def test_client():
    c = ClientGRPC(port=50051)
    r = await c.create_game(['elenzo', 'lajuli'])
    print(f'Received {r.turn_data}\n\n')
    r = await c.execute_action(
        r.game_id,
        {
            'action': 'move',
            'data': {
                'from_row': 0,
                'from_col': 4,
                'to_row': 1,
                'to_col': 4,
            },
        },
    )
    print(f'Received {r.turn_data}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_client())
    loop.run_forever()
