import asyncio

semaphore  = asyncio.Semaphore(5)

async def limited_fetch(session,url):
    async with semaphore:
        async with session.get(url) as response : 
            return await response.json()


            