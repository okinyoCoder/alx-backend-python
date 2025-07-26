import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect("user.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = cursor.fetchall()
            print("All users: ", users)
            return users

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect("example.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            print("Users older than 40:", older_users)
            return older_users

# Run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )