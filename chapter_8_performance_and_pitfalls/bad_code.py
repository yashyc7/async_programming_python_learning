# Fix it completely:

# Requirements
# Replace blocking code
# Make it truly concurrent
# Add timeout
# Add error handling
# Use gather
# Ensure no crash

import asyncio
import time
import requests

async def fetch_data(i):
    time.sleep(1)  # blocking
    return requests.get(f"https://jsonplaceholder.typicode.com/todos/{i}").json()

async def main():
    results = []
    for i in range(5):
        results.append(await fetch_data(i))  # sequential

    print(results)

asyncio.run(main())