from fastapi import BackgroundTasks

def log_task(data):
    print("Logging",data)

@app.get("/process")
async def processs(background_tasks:BackgroundTasks):
    background_tasks.add_task(log_task,"some_data")
    return {"status":"processing"}


#fire and forget is for the backgroundtasks we can use it for the logging 