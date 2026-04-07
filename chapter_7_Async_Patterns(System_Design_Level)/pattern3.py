import asyncio 

semaphore = asyncio.Semaphore(3)



async def limited_fetch(id):
    async with semaphore:
        print(f"fetching {id}")
        await asyncio.sleep(1)
        return id 

        
# this only run the 3 tasks run at at time 
