# performing solution using the async progrmming 
import asyncio

async def fetch_data(integer : int)->str :
    await asyncio.sleep(2) #non blocking wait 
    return "data" + str(integer)

async def main():
    results  = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

asyncio.run(main())

# returns this ['data1', 'data2', 'data3']

# What happens now?
# All 3 start together
# Wait happens in parallel (concurrently)
# Total time ≈ 2 seconds


# 🧩 Important Distinction
# ❌ Async ≠ Parallelism
# Concept	Meaning
# Concurrency	Handling multiple tasks at once
# Parallelism	Running on multiple CPUs simultaneously

# 👉 Async = Concurrency (single thread, smart scheduling)

# 🧨 Critical Rule (Most People Miss This)

# Async only helps when:

# Tasks are waiting (I/O)

# Async does NOT help when:

# Heavy CPU work (e.g., image processing)

# 🧪 Example Comparison
# Sync Timing
# # 3 tasks × 2 sec each = 6 sec
# Async Timing
# # All overlap → ~2 sec total

# 👉 That’s a 3x improvement without extra hardware