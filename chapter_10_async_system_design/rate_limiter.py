import asyncio

class RateLimiter:
    """Controls max concurrent tasks at any moment"""

    def __init__(self,max_concurrent:int) -> None:
        self._semaphore=asyncio.Semaphore(max_concurrent)

    async def __aenter__(self):
        await self._semaphore.acquire()
        return self
    async def __aexit__(self,*args):
        self._semaphore.release()