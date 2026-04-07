# this is wrong below 

import sqlite3  #blocking


# what we can do instead is to use the 

# ✅ Correct tools
# asyncpg (PostgreSQL)
# databases
# SQLAlchemy async

# also the correct practise is like this 

# async def get_user():
#     return await db.fetch_one(...)