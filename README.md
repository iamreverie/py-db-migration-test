```
pip install asyncpg alembic psycopg2-binary
```

**Alembic Setup**
```
alembic init migrations
```

**Create First Migration**
```
alembic revision -m "create users table"
```

**Run Migration**
```
alembic upgrade head
```

**Alembic Downgrade**
```
alembic downgrade -1
```