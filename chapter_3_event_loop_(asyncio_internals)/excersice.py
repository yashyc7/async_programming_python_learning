# 🧪 Exercise (Important)
# Task

# Create 3 coroutines:

# task("A", 3)
# task("B", 1)
# task("C", 2)
# Requirements:
# Log:
# Start time
# End time
# Use asyncio.gather
# Observe execution order
import asyncio
import time

async def execute(task:str,delay_time:int)->None: 
    print(f"task {task} started at {time.strftime('%X')} ")
    await asyncio.sleep(delay_time)
    print(f"task {task} ended at {time.strftime('%X')} ")

async def main():
    results = await asyncio.gather(
        execute("A",3),
        execute("B",1),
        execute("C",2)
    )
    print(results)


# A started at 21:02:31
# B started at 21:02:31
# C started at 21:02:31
# B started at 21:02:32
# A started at 21:02:33
# C started at 21:02:34