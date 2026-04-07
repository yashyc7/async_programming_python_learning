from fastapi import FastAPI
import asyncio

app = asyncio()

@app.get('/')
async def root():
    await asyncio.sleep(1)
    return {"message":"Hello async"}


# 🧠 What happens
# Request comes in
# await yields control
# Server handles other requests