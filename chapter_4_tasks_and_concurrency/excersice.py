import asyncio
import time

async def work(task,delay):
    print(f"{task} started at {time.strftime("%X")}")
    await asyncio.sleep(delay)
    print(f"{task} ended at {time.strftime("%X")}")
    return task

async def main():
    task1 = asyncio.create_task(work("A",3))
    task2 = asyncio.create_task(work("B",1))
    task3 = asyncio.create_task(work("C",2))

    print("All tasks started ")

    result1= await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())
    
# All tasks started 
# A started at 21:34:09
# B started at 21:34:09
# C started at 21:34:09
# B ended at 21:34:10
# C ended at 21:34:11
# A ended at 21:34:12
# A B C