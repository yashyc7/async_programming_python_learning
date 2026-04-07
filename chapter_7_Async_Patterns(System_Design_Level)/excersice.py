# 🧪 Exercise (Important)
# Task — Build Controlled Async Worker System
# Requirements
# 1. Producer
# Generate numbers 1 → 20
# Push into queue
# 2. Consumers (2–3 workers)
# Pull from queue
# Simulate API call (asyncio.sleep)

# Print:

# Worker-1 processed 5
# 3. Add Backpressure
# Queue(maxsize=5)
# 4. Add Rate Limiting
# Use Semaphore(3)
# Only 3 tasks processed concurrently
# 5. Graceful Shutdown
# Use:
# await queue.join()
# Cancel workers after done

# 🧠 What You Should Learn

# After this:

# How to control concurrency, not just create it
# How to protect systems under load
# How to design scalable pipelines
# 🚨 Common Mistakes
# Infinite consumers without cancellation ❌
# No queue limits ❌
# No rate limiting ❌
# Overloading external APIs ❌


import asyncio

queue = asyncio.Queue(maxsize=5)  # ✅ backpressure
semaphore = asyncio.Semaphore(3)  # ✅ rate limiting


# 🔹 Producer
async def producer():
    for i in range(1, 21):
        await queue.put(i)  # ✅ FIXED
        print(f"Produced {i}")
        await asyncio.sleep(0.2)


# 🔹 Consumer
async def consumer(name):
    try:
        while True:
            item = await queue.get()

            async with semaphore:  # ✅ rate limiting
                print(f"{name} processing {item}")
                await asyncio.sleep(1)

            queue.task_done()

    except asyncio.CancelledError:
        print(f"{name} shutting down")
        raise


# 🔹 Main Orchestrator
async def main():
    producers = [asyncio.create_task(producer())]

    consumers = [
        asyncio.create_task(consumer("Worker-1")),
        asyncio.create_task(consumer("Worker-2")),
        asyncio.create_task(consumer("Worker-3")),
    ]

    # wait for producer to finish
    await asyncio.gather(*producers)

    # wait until all tasks processed
    await queue.join()

    # cancel consumers
    for c in consumers:
        c.cancel()

    # wait for proper shutdown
    await asyncio.gather(*consumers, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())

# Produced 1
# Worker-1 processing 1
# Produced 2
# Worker-2 processing 2
# Produced 3
# Worker-3 processing 3
# Produced 4
# Produced 5
# Worker-1 processing 4
# Produced 6
# Worker-2 processing 5
# Produced 7
# Produced 8
# Worker-3 processing 6
# Produced 9
# Produced 10
# Worker-1 processing 7
# Produced 11
# Worker-2 processing 8
# Produced 12
# Produced 13
# Worker-3 processing 9
# Produced 14
# Worker-1 processing 10
# Produced 15
# Worker-2 processing 11
# Produced 16
# Worker-3 processing 12
# Produced 17
# Worker-1 processing 13
# Produced 18
# Worker-2 processing 14
# Produced 19
# Worker-3 processing 15
# Produced 20
# Worker-1 processing 16
# Worker-2 processing 17
# Worker-3 processing 18
# Worker-1 processing 19
# Worker-2 processing 20
# Worker-1 shutting down
# Worker-2 shutting down
# Worker-3 shutting down