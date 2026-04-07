import asyncio

async def fake_api_call(id):
    await asyncio.sleep(2)
    return 2

async def main():
    results = await asyncio.gather(
        fake_api_call(1),
        fake_api_call(2),
        fake_api_call(3),
        fake_api_call(4),
        fake_api_call(5),
    )

    print(results[0]) # since i got the arrays of 2 . 

asyncio.run(main())