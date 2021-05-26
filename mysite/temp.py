import asyncio


async def store_data_of_video():
    print('Lol')
    await asyncio.sleep(1)
    await store_data_of_video()

asyncio.run(store_data_of_video())