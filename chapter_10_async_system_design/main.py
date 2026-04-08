import asyncio
import aiohttp
from fetcher import fetch_with_retry
from rate_limiter import RateLimiter
from logger import get_logger

logger = get_logger("main")

# --- Config ---
URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
MAX_CONCURRENT = 5   # max tasks at once
RETRIES = 3
TIMEOUT = 5.0


async def run_aggregator(urls: list[str]) -> list[dict]:
    limiter = RateLimiter(MAX_CONCURRENT)
    results = []

    async def bounded_fetch(session, url, task_id):
        async with limiter:
            return await fetch_with_retry(session, url, task_id, RETRIES, TIMEOUT)

    async with aiohttp.ClientSession() as session:
        tasks = [
            bounded_fetch(session, url, idx)
            for idx, url in enumerate(urls, start=1)
        ]
        results = await asyncio.gather(*tasks)

    return list(results)


async def main():
    logger.info(f"Starting aggregator for {len(URLS)} URLs")
    results = await run_aggregator(URLS)

    success = [r for r in results if r["status"] == "success"]
    failed  = [r for r in results if r["status"] == "failed"]

    logger.info(f"Done — ✓ {len(success)} success | ✗ {len(failed)} failed")
    return results


if __name__ == "__main__":
    asyncio.run(main())