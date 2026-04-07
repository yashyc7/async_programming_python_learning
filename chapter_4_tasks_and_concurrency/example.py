import asyncio
import time 

async def work(name,delay):
    print(f"{name} started at {time.strftime("%X")}")
    await asyncio.sleep(delay)
    print(f"{name} ended at {time.strftime("%X")}")
    return name 

async def main():
    task1 = asyncio.create_task(work("A",3))
    task2 = asyncio.create_task(work("B",1))
    task3 = asyncio.create_task(work("C",2))
    print("Tasks started ... ")

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())

# Tasks started ... 
# A started at 21:23:42
# B started at 21:23:42
# C started at 21:23:42
# B ended at 21:23:43
# C ended at 21:23:44
# A ended at 21:23:45
# A B C


# 🧠 What’s happening here
# Tasks start immediately (don’t wait)
# You control when to await
# Execution is concurrent


# Key Insight
# task = create_task(...)

# 👉 means:

# “Start this now, I’ll deal with result later”


# asyncio.create_task(work("A", 5))

# 👉 You don’t await it

# Risk:
# Task may fail silently
# Hard to debug
# Memory leaks