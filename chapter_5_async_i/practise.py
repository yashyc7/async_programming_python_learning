import asyncio
import aiohttp
import time 

import asyncio
import aiohttp
import time

async def fetch(session, id):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    
    print(f"Start {id} at {time.strftime('%X')}")
    
    async with session.get(url) as response:
        data = await response.json()
    
    print(f"End {id} at {time.strftime('%X')}")
    
    return data

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session: 
        tasks = [
            fetch(session,1),
            fetch(session,2),
            fetch(session,3),
            fetch(session,4),
            fetch(session,5)
        ]
        results = await asyncio.gather(*tasks)

        end = time.time()

        print(results)

        print(f"Total time: {end-start:.2f}sec")
    
asyncio.run(main())



# Start 1 at 23:18:42
# Start 2 at 23:18:42
# Start 3 at 23:18:42
# Start 4 at 23:18:42
# Start 5 at 23:18:42
# End 3 at 23:18:43
# End 2 at 23:18:43
# End 1 at 23:18:43
# End 5 at 23:18:43
# End 4 at 23:18:45
# [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}, {'userId': 1, 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum', 'completed': False}]
# Total time: 2.19sec