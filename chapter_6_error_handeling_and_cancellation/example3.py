import asyncio

async def work():
    try:
        print("Working...")
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise 

async def main():
    task = asyncio.create_task(work())

    await asyncio.sleep(2)
    task.cancel()

    try : 
        await task
    except asyncio.CancelledError:
        print("Handelled cancellation")

asyncio.run(main())


# Working...
# Task was cancelled
# Handelled cancellation