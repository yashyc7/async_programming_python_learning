# 🧪 Exercise (Real Backend)
# 🎯 Build This API
# Endpoint:
# GET /aggregate
# Requirements
# 1. Fetch 5 todos concurrently
# 2. Add timeout (2 sec)
# 3. Add retry (2 attempts)
# 4. Return:
# {
#   "data": [...],
#   "errors": [...]
# }

import asyncio
import aiohttp


# 🔹 Layer 1 — Raw Fetch
async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


# 🔹 Layer 2 — Safe Fetch (retry + timeout)
async def safe_fetch(session: aiohttp.ClientSession, url: str, retries: int = 2) -> dict:
    for attempt in range(retries + 1):
        try:
            return await asyncio.wait_for(fetch(session, url), timeout=2)

        except asyncio.TimeoutError:
            if attempt == retries:
                return {"error": "timeout"}

        except Exception:
            if attempt == retries:
                return {"error": "failed"}

        await asyncio.sleep(0.5)  # small backoff


# 🔹 Layer 3 — Orchestrator
async def main():
    base_url = "https://jsonplaceholder.typicode.com/todos/{}"

    async with aiohttp.ClientSession() as session:
        tasks = [
            safe_fetch(session, base_url.format(i))
            for i in range(1, 6)
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        print(results)


if __name__ == "__main__":
    asyncio.run(main())