import asyncpg
from config import ASYNC_DATABASE_URL

class Database:
    """Async context manager for PostgreSQL connections."""

    def __init__(self, dsn: str = ASYNC_DATABASE_URL):
        self._dsn = dsn
        self._pool = None

    async def connect(self):
        if not self._pool:
            self._pool = await asyncpg.create_pool(dsn=self._dsn, min_size=1, max_size=5)
        return self._pool

    async def close(self):
        if self._pool:
            await self._pool.close()
            self._pool = None

    async def fetch(self, query: str, *args):
        async with self._pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query: str, *args):
        async with self._pool.acquire() as conn:
            return await conn.execute(query, *args)
