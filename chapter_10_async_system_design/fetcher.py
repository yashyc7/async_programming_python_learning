import asyncio
import aiohttp
from logger import get_logger

logger = get_logger("fetcher")

async def fetch_with_retry(
    session: aiohttp.ClientSession,
    url: str,
    task_id: int,
    retries: int = 3,
    timeout: float = 5.0,
) -> dict:
    for attempt in range(1, retries + 1):
        try:
            logger.info(f"[Task {task_id}] Attempt {attempt} → {url}")

            # ✅ await first, then async with
            response = await asyncio.wait_for(session.get(url), timeout=timeout)
            async with response:
                data = await response.json()
                logger.info(f"[Task {task_id}] ✓ Success on attempt {attempt}")
                return {"task_id": task_id, "status": "success", "data": data}

        except asyncio.TimeoutError:
            logger.warning(f"[Task {task_id}] Timeout on attempt {attempt}")

        except Exception as e:
            logger.error(f"[Task {task_id}] Error on attempt {attempt}: {e}")

        if attempt < retries:
            backoff = 2 ** attempt
            logger.info(f"[Task {task_id}] Retrying in {backoff}s...")
            await asyncio.sleep(backoff)

    logger.error(f"[Task {task_id}] ✗ All {retries} attempts failed")
    return {"task_id": task_id, "status": "failed", "data": None}


#2026-04-08 16:53:01,234 | INFO | main | Starting aggregator for 20 URLs2026-04-08 16:53:01,236 | INFO | fetcher | [Task 1] Attempt 1 → https://jsonplaceholder.typicode.com/posts/1
# 2026-04-08 16:53:01,245 | INFO | fetcher | [Task 2] Attempt 1 → https://jsonplaceholder.typicode.com/posts/2
# 2026-04-08 16:53:01,246 | INFO | fetcher | [Task 3] Attempt 1 → https://jsonplaceholder.typicode.com/posts/3
# 2026-04-08 16:53:01,246 | INFO | fetcher | [Task 4] Attempt 1 → https://jsonplaceholder.typicode.com/posts/4
# 2026-04-08 16:53:01,247 | INFO | fetcher | [Task 5] Attempt 1 → https://jsonplaceholder.typicode.com/posts/5
# 2026-04-08 16:53:01,814 | INFO | fetcher | [Task 1] ✓ Success on attempt 1
# 2026-04-08 16:53:01,872 | INFO | fetcher | [Task 6] Attempt 1 → https://jsonplaceholder.typicode.com/posts/6
# 2026-04-08 16:53:01,887 | INFO | fetcher | [Task 3] ✓ Success on attempt 1
# 2026-04-08 16:53:01,890 | INFO | fetcher | [Task 4] ✓ Success on attempt 1
# 2026-04-08 16:53:01,902 | INFO | fetcher | [Task 5] ✓ Success on attempt 1
# 2026-04-08 16:53:01,955 | INFO | fetcher | [Task 7] Attempt 1 → https://jsonplaceholder.typicode.com/posts/7
# 2026-04-08 16:53:01,979 | INFO | fetcher | [Task 8] Attempt 1 → https://jsonplaceholder.typicode.com/posts/8
# 2026-04-08 16:53:01,982 | INFO | fetcher | [Task 9] Attempt 1 → https://jsonplaceholder.typicode.com/posts/9
# 2026-04-08 16:53:02,028 | INFO | fetcher | [Task 6] ✓ Success on attempt 1
# 2026-04-08 16:53:02,029 | INFO | fetcher | [Task 10] Attempt 1 → https://jsonplaceholder.typicode.com/posts/10
# 2026-04-08 16:53:02,085 | INFO | fetcher | [Task 8] ✓ Success on attempt 1
# 2026-04-08 16:53:02,091 | INFO | fetcher | [Task 11] Attempt 1 → https://jsonplaceholder.typicode.com/posts/11
# 2026-04-08 16:53:02,103 | INFO | fetcher | [Task 7] ✓ Success on attempt 1
# 2026-04-08 16:53:02,104 | INFO | fetcher | [Task 12] Attempt 1 → https://jsonplaceholder.typicode.com/posts/12
# 2026-04-08 16:53:02,111 | INFO | fetcher | [Task 9] ✓ Success on attempt 1
# 2026-04-08 16:53:02,113 | INFO | fetcher | [Task 13] Attempt 1 → https://jsonplaceholder.typicode.com/posts/13
# 2026-04-08 16:53:02,133 | INFO | fetcher | [Task 10] ✓ Success on attempt 1
# 2026-04-08 16:53:02,134 | INFO | fetcher | [Task 14] Attempt 1 → https://jsonplaceholder.typicode.com/posts/14
# 2026-04-08 16:53:02,209 | INFO | fetcher | [Task 11] ✓ Success on attempt 1
# 2026-04-08 16:53:02,210 | INFO | fetcher | [Task 15] Attempt 1 → https://jsonplaceholder.typicode.com/posts/15
# 2026-04-08 16:53:02,211 | INFO | fetcher | [Task 12] ✓ Success on attempt 1
# 2026-04-08 16:53:02,212 | INFO | fetcher | [Task 16] Attempt 1 → https://jsonplaceholder.typicode.com/posts/16
# 2026-04-08 16:53:02,217 | INFO | fetcher | [Task 13] ✓ Success on attempt 1
# 2026-04-08 16:53:02,218 | INFO | fetcher | [Task 17] Attempt 1 → https://jsonplaceholder.typicode.com/posts/17
# 2026-04-08 16:53:02,235 | INFO | fetcher | [Task 14] ✓ Success on attempt 1
# 2026-04-08 16:53:02,236 | INFO | fetcher | [Task 18] Attempt 1 → https://jsonplaceholder.typicode.com/posts/18
# 2026-04-08 16:53:02,267 | INFO | fetcher | [Task 2] ✓ Success on attempt 1
# 2026-04-08 16:53:02,267 | INFO | fetcher | [Task 19] Attempt 1 → https://jsonplaceholder.typicode.com/posts/19
# 2026-04-08 16:53:02,315 | INFO | fetcher | [Task 15] ✓ Success on attempt 1
# 2026-04-08 16:53:02,318 | INFO | fetcher | [Task 16] ✓ Success on attempt 1
# 2026-04-08 16:53:02,320 | INFO | fetcher | [Task 20] Attempt 1 → https://jsonplaceholder.typicode.com/posts/20
# 2026-04-08 16:53:02,322 | INFO | fetcher | [Task 17] ✓ Success on attempt 1
# 2026-04-08 16:53:02,341 | INFO | fetcher | [Task 18] ✓ Success on attempt 1
# 2026-04-08 16:53:02,430 | INFO | fetcher | [Task 20] ✓ Success on attempt 1
# 2026-04-08 16:53:02,478 | INFO | fetcher | [Task 19] ✓ Success on attempt 1
# 2026-04-08 16:53:02,552 | INFO | main | Done — ✓ 20 success | ✗ 0 failed