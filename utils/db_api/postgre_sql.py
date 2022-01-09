from typing import Union

import asyncpg
from asyncpg import Pool, Connection

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result

    async def create_table_accounts(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Prices(
        id SERIAL PRIMARY KEY,
        name BIGINT NOT NULL, 
        data VARCHAR(255) NULL UNIQUE ,
        price VARCHAR(510) NULL UNIQUE,
        );
        """
        await self.execute(sql, execute=True)

    async def select_all_account(self):
        sql = "SELECT * FROM Prices"
        return await self.execute(sql, fetch=True)

    async def select_dates_by_name(self, coin_name):
        sql = "SELECT data FROM Prices WHERE name=$1"
        return await self.execute(sql, coin_name, fetchrow=True)

    async def select_price_by_coin_name(self, coin_name, data):
        sql = "SELECT price FROM Prices WHERE name=$1 AND data=$2"
        return await self.execute(sql, coin_name, data, fetchrow=True)
