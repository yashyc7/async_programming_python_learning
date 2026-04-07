import asyncio

queue = asyncio.Queue(maxsize=5)  # limit = backpressure


# 🔹 Producer
async def producer():
    for i in range(10):
        await queue.put(i)
        print(f"Produced {i}")
        await asyncio.sleep(0.2)


# 🔹 Consumer
async def consumer(name):
    while True:
        item = await queue.get()
        print(f"{name} consuming {item}")

        await asyncio.sleep(1)  # simulate work

        queue.task_done()


async def main():
    producers = [asyncio.create_task(producer())]
    consumers = [
        asyncio.create_task(consumer("C1")),
        asyncio.create_task(consumer("C2")),
    ]

    await asyncio.gather(*producers)
    await queue.join()  # wait until all items are processed

    for c in consumers:
        c.cancel() # 👉 Stop infinite loops


asyncio.run(main())


# Produced 0
# C1 consuming 0
# Produced 1
# C2 consuming 1
# Produced 2
# Produced 3
# Produced 4
# C1 consuming 2
# Produced 5
# C2 consuming 3
# Produced 6
# Produced 7
# Produced 8
# C1 consuming 4
# Produced 9
# C2 consuming 5
# C1 consuming 6
# C2 consuming 7
# C1 consuming 8
# C2 consuming 9