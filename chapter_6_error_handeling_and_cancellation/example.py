import asyncio

async def good():
    await asyncio.sleep(1)
    return "OK"

async def bad():
    await asyncio.sleep(1)
    raise Exception("Boom broken")

async def main():
    results = await asyncio.gather(
        good(),
        bad(),
        return_exceptions=True
    )

    print(results)

asyncio.run(main())

# ['OK', Exception('Boom broken')]