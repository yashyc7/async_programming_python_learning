#route 

@app.get('/todos')
async def todos():
    return await todo_service.get_all()

#service 
async def get_all():
    return await client.fetch_all()