import asyncio 

async def fetch_user():
    await asyncio.sleep(2)
    print("fetching the users after 2 seconds")
    return {"name":"yash","id":1}

async def fetch_orders():
    await asyncio.sleep(4)
    print("fetching the users after 4 seconds")
    return ["order1","order2"]

async def fetch_payments(): 
    await asyncio.sleep(6)
    print("fetching the users after 6 seconds")
    return ["payment1","payment2"]


async def main():
    print(await fetch_user())
    print(await fetch_orders())
    print(await fetch_payments())


asyncio.run(main())
# it is still fetching the data sequentially because we didn't used the gather or create task here we would cover it in the next chapter 
# it works like normal function calling hence no use 
# fetching the users after 2 seconds
# {'name': 'yash', 'id': 1}
# fetching the users after 4 seconds
# ['order1', 'order2']
# fetching the users after 6 seconds
# ['payment1', 'payment2']