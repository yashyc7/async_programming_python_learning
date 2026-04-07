from fastapi import Depends
import aiohttp 
async def get_session():
    async with aiohttp.ClientSession() as session: 
        yield session


@app.get("/todos")
async def get_todos(session=Depends(get_session)):
    async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response : 
        return await response.json()
        