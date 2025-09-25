import asyncio
from db import Database

async def run():
    db = Database()
    await db.connect()

    # Example: Insert
    # await db.execute("INSERT INTO users (name) VALUES ($1)", "Alice")

    # Example: Select
    # rows = await db.fetch("SELECT * FROM users")
    rows = await db.fetch("SELECT version();")
    for row in rows:
        print(dict(row))

    await db.close()

if __name__ == "__main__":
    asyncio.run(run())
