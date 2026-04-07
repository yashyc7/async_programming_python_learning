import asyncio 
import aiohttp


#Layer 1 -Raw fetch (no logic here)
async def fetch(session:aiohttp.ClientSession,url:str)->dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()  # pause execution untill json didnt come 

#layer 2 - safe fetch(timeout+retry+error handeling)
async def safe_fetch(session:aiohttp.ClientSession,url:str,retries:int = 2 )->dict:
    for attempt in range(retries+1):
        try:
            return await asyncio.wait_for(fetch(session,url),timeout=2)
        except asyncio.TimeoutError:
            if attempt==retries:
                return {"error":"timeout"}
        except Exception as e:
            if attempt == retries:
                return {"error":"failed after retries"}
        #small delay before retry (except last attempt)
        await asyncio.sleep(0.5)

#layer 3 orchestrator

async def main():
    base_url="https://jsonplaceholder.typicode.com/todos/{}"

    async with aiohttp.ClientSession() as session:
        tasks = [
            safe_fetch(session,base_url.format(i)) for i in range(1,50)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        print(results)

asyncio.run(main())


# [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}, {'userId': 1, 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum', 'completed': False}]

# now try with the "https://httpstat.us/200?sleep=5000"
# we are getting this now the slow one 

# [{'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}]

# now the force failure one link below 
#"https://jsonplaceholder.typicode.com/invalid"

# [{'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}, {'error': 'failed after retries'}]

# increasing load from 1 to 5 from 1 to 50
# still got results very faster 

# [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}, {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}, {'userId': 1, 'id': 4, 'title': 'et porro tempora', 'completed': True}, {'userId': 1, 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum', 'completed': False}, {'userId': 1, 'id': 6, 'title': 'qui ullam ratione quibusdam voluptatem quia omnis', 'completed': False}, {'userId': 1, 'id': 7, 'title': 'illo expedita consequatur quia in', 'completed': False}, {'userId': 1, 'id': 8, 'title': 'quo adipisci enim quam ut ab', 'completed': True}, {'userId': 1, 'id': 9, 'title': 'molestiae perspiciatis ipsa', 'completed': False}, {'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True}, {'userId': 1, 'id': 11, 'title': 'vero rerum temporibus dolor', 'completed': True}, {'userId': 1, 'id': 12, 'title': 'ipsa repellendus fugit nisi', 'completed': True}, {'userId': 1, 'id': 13, 'title': 'et doloremque nulla', 'completed': False}, {'userId': 1, 'id': 14, 'title': 'repellendus sunt dolores architecto voluptatum', 'completed': True}, {'userId': 1, 'id': 15, 'title': 'ab voluptatum amet voluptas', 'completed': True}, {'userId': 1, 'id': 16, 'title': 'accusamus eos facilis sint et aut voluptatem', 'completed': True}, {'userId': 1, 'id': 17, 'title': 'quo laboriosam deleniti aut qui', 'completed': True}, {'userId': 1, 'id': 18, 'title': 'dolorum est consequatur ea mollitia in culpa', 'completed': False}, {'userId': 1, 'id': 19, 'title': 'molestiae ipsa aut voluptatibus pariatur dolor nihil', 'completed': True}, {'userId': 1, 'id': 20, 'title': 'ullam nobis libero sapiente ad optio sint', 'completed': True}, {'userId': 2, 'id': 21, 'title': 'suscipit repellat esse quibusdam voluptatem incidunt', 'completed': False}, {'userId': 2, 'id': 22, 'title': 'distinctio vitae autem nihil ut molestias quo', 'completed': True}, {'userId': 2, 'id': 23, 'title': 'et itaque necessitatibus maxime molestiae qui quas velit', 'completed': False}, {'userId': 2, 'id': 24, 'title': 'adipisci non ad dicta qui amet quaerat doloribus ea', 'completed': False}, {'userId': 2, 'id': 25, 'title': 'voluptas quo tenetur perspiciatis explicabo natus', 'completed': True}, {'userId': 2, 'id': 26, 'title': 'aliquam aut quasi', 'completed': True}, {'userId': 2, 'id': 27, 'title': 'veritatis pariatur delectus', 'completed': True}, {'userId': 2, 'id': 28, 'title': 'nesciunt totam sit blanditiis sit', 'completed': False}, {'userId': 2, 'id': 29, 'title': 'laborum aut in quam', 'completed': False}, {'userId': 2, 'id': 30, 'title': 'nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis', 'completed': True}, {'userId': 2, 'id': 31, 'title': 'repudiandae totam in est sint facere fuga', 'completed': False}, {'userId': 2, 'id': 32, 'title': 'earum doloribus ea doloremque quis', 'completed': False}, {'userId': 2, 'id': 33, 'title': 'sint sit aut vero', 'completed': False}, {'userId': 2, 'id': 34, 'title': 'porro aut necessitatibus eaque distinctio', 'completed': False}, {'userId': 2, 'id': 35, 'title': 'repellendus veritatis molestias dicta incidunt', 'completed': True}, {'userId': 2, 'id': 36, 'title': 'excepturi deleniti adipisci voluptatem et neque optio illum ad', 'completed': True}, {'userId': 2, 'id': 37, 'title': 'sunt cum tempora', 'completed': False}, {'userId': 2, 'id': 38, 'title': 'totam quia non', 'completed': False}, {'userId': 2, 'id': 39, 'title': 'doloremque quibusdam asperiores libero corrupti illum qui omnis', 'completed': False}, {'userId': 2, 'id': 40, 'title': 'totam atque quo nesciunt', 'completed': True}, {'userId': 3, 'id': 41, 'title': 'aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit', 'completed': False}, {'userId': 3, 'id': 42, 'title': 'rerum perferendis error quia ut eveniet', 'completed': False}, {'userId': 3, 'id': 43, 'title': 'tempore ut sint quis recusandae', 'completed': True}, {'userId': 3, 'id': 44, 'title': 'cum debitis quis accusamus doloremque ipsa natus sapiente omnis', 'completed': True}, {'userId': 3, 'id': 45, 'title': 'velit soluta adipisci molestias reiciendis harum', 'completed': False}, {'userId': 3, 'id': 46, 'title': 'vel voluptatem repellat nihil placeat corporis', 'completed': False}, {'userId': 3, 'id': 47, 'title': 'nam qui rerum fugiat accusamus', 'completed': False}, {'userId': 3, 'id': 48, 'title': 'sit reprehenderit omnis quia', 'completed': False}, {'userId': 3, 'id': 49, 'title': 'ut necessitatibus aut maiores debitis officia blanditiis velit et', 'completed': False}]