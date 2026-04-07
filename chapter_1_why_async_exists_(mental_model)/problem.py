# 🔥 Core Problem

# Normal Python code is blocking.

import time

def fetch_data():
    time.sleep(2) #simulate api call 
    return "data"

def main():
    print(fetch_data())
    print(fetch_data())
    print(fetch_data())

main()

# output is like below 

# data
# data
# data


# What happens?
# Call 1 → waits 2 sec
# Call 2 → waits 2 sec
# Call 3 → waits 2 sec

# 👉 Total = 6 seconds

# This is sequential blocking execution.

# 🧠 Key Insight

# Most backend systems are I/O bound, not CPU bound.

# I/O-bound = waiting
# API calls
# DB queries
# File reads
# Network

# 👉 CPU is idle, just waiting.


# ⚔️ Sync vs Async Thinking
# Sync (Blocking)

# "Do one thing at a time, wait until it's done."

# Async (Non-blocking)

# "Start work, don’t wait, handle other work while waiting."

# 🏎️ Real-World Analogy
# Sync waiter:
# Takes order
# Goes to kitchen
# Waits there
# Comes back
# Async waiter:
# Takes order
# Sends to kitchen
# Serves other tables meanwhile

# 👉 Same time, more work done