import asyncio
import aiohttp 
from fastapi import FastAPI 


app = FastAPI()

async def fetch(session,i):
    url = f"https://jsonplaceholder.typicode.com/todos/{i}"
    async with session.get(url) as response : 
        return await response.json()


@app.get('/todos')
async def get_todos():
    async with aiohttp.ClientSession() as session : 
        tasks = [fetch(session,i) for i in range(1,6)]
        results = await asyncio.gather(*tasks)
    return results 