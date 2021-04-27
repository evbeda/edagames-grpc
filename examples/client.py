import asyncio
from edagames_grpc.client import ClientGRPC


async def test_client():
    c = ClientGRPC()
    await c.start()
    r = await c.create_game(['asd'])
    print(f'Received {r}')
    r = await c.execute_action(
        '0000-0002',
        {
            'action': 'asd',
            'data': {
                'clave': 'otro asd',
                'otra clave': 'mas asdasd',
            },
        },
    )
    print(f'Received {r}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_client())
    loop.run_forever()
