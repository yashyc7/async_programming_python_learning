import asyncio
import time 
async def task(name,delay_time):
    print(f"{name} started at {time.strftime('%X')}")
    await asyncio.sleep(delay_time)
    print(f"{name} started at {time.strftime('%X')}")

async def main():
    await asyncio.gather(
        task("A",2),
        task("B",1),
        task("C",3),
        )
asyncio.run(main())

#all three tasks started at the same time 
# but the task B started first then it finished earlier due to 1 second wait and hence
# task A executed due to 2 second wait 
# lastly task C executed with 3 second wait 

# A started at 20:26:58
# B started at 20:26:58
# C started at 20:26:58
# B started at 20:26:59
# A started at 20:27:00
# C started at 20:27:01

# finding even though A started first , B finishes first because of less await sleep time 


# ⚡ Key Insight

# Event loop is:

# Not FIFO (first-in-first-out execution)

# It is:

# Completion-driven scheduling


# 🔬 Internal Model (Keep This in Mind)

# Think of event loop as:

# while tasks_exist:
#     pick_ready_task
#     run_until_await
#     store_task_state
#     switch_to_next_task


# 🧨 Critical Rule
# blocks the event loop (time.sleep blocks the event loop)
# If you block the loop → everything stops

# async def bad_task():
#     time.sleep(5)  # ❌ blocks entire event loop

# 👉 NEVER use blocking calls inside async