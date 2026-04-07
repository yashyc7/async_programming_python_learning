import asyncio

async def fetch_user():
    await asyncio.sleep(1)
    return {"id":1 , "name":"Yash"}


async def fetch_orderes(): 
    await asyncio.sleep(1)
    return ["order1","order2"]

async def main():
    user = await fetch_user()
    order = await fetch_orderes()
    print(user)
    print(order)

asyncio.run(main()) #creates the event loop and manages the async funtions as they returns the coroutine 

# {'id': 1, 'name': 'Yash'}
# ['order1', 'order2']
# (async_programming_python_l

# ⚠️ Important:

# This is still sequential async, not concurrent.

# 👉 Why?
# Because:

# await fetch_user()
# await fetch_orders()

# Runs one after another.

# 🧠 Key Insight

# Async ≠ automatic concurrency

# You control concurrency using:

# create_task
# gather (next chapter)