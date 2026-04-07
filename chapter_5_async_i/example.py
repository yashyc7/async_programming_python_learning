import aiohttp
import asyncio
import time

URL = "https://jsonplaceholder.typicode.com/todos/1"

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, URL),
            fetch(session, URL),
            fetch(session, URL),
            fetch(session, URL),
            fetch(session, URL),
        ]

        results = await asyncio.gather(*tasks)

    end = time.time()

    print(results)
    print(f"Total time: {end - start:.2f} sec")

asyncio.run(main())

# 🧠 What’s happening
# 5 HTTP requests fired together
# No blocking
# Event loop handles responses

# 👉 Total time ≈ 1 request time, not 5

# ⚙️ Under the Hood

# When you do:

# await session.get(url)

# 👉 It:

# Sends request
# Yields control
# Event loop handles other tasks
# Resumes when response arrives
# 🔥 Real Backend Impact
# Sync server:
# 1000 users → 1000 threads (heavy)
# Async server:
# 1000 users → 1 thread + event loop

# 👉 Massive scalability gain

# ⚠️ Critical Rules (Production)
# ❌ NEVER do this:
# import requests

# async def fetch():
#     requests.get(...)  # ❌ blocking inside async

# 👉 You kill the event loop

# ✅ Always use async-compatible libs
# Domain	Async Library
# HTTP	aiohttp, httpx
# DB	asyncpg, databases
# File	aiofiles
# 🧪 Exercise (Real-World)
# Task

# Build an async API aggregator.