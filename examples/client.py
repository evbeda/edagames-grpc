import asyncio
from edagames_grpc.client import ClientGRPC


async def test_client():
    c = ClientGRPC(port=50051)
    r = await c.create_game(['elenzo', 'lajuli'])
    print(f'Received {r}')
    r = await c.execute_action(
        r.game_id,
        {
            'action': 'move',
            'data': {
                'from_row': 1,
                'from_col': 2,
                'to_rol': 1,
                'to_col': 2,
            },
        },
    )
    print(f'Received {r}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_client())
    loop.run_forever()
