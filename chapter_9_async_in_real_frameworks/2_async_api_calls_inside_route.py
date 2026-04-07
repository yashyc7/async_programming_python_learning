import aiohttp 

@app.get("/data")
async def get_data():
    async with aiohttp.ClientSession() as session : 
        async with sesion.get("https://jsonplaceholder.typicode.com/todos/1") as response : 
            return await response.json()

# above version is correct 


# below version is wrong 

import requests

@app.get("/data")
async def get_data():
    return requests.get("https://api.com").json()  # ❌