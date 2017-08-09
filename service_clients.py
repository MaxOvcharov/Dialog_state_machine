import aiopg.sa


class PostgreSQLClient:
    """ PostgreSQL connection pool client """

    def __init__(self, loop, conf):
        self.loop = loop
        self.conf = conf

    @classmethod
    async def connect(cls):
        # TODO CREATE ENTRY POINT FOR CLIENT FACTORY
        pass

    async def _connection(self):
        self.pg = await aiopg.sa.create_engine(
            database=self.conf['database'],
            user=self.conf['user'],
            password=self.conf['password'],
            host=self.conf['host'],
            port=self.conf['port'],
            minsize=self.conf['minsize'],
            maxsize=self.conf['maxsize'],
            loop=self.loop)

    async def close_connection(self):
        self.pg.close()
        await self.pg.wait_closed()


async def pg_client_factory(loop, conf, client=PostgreSQLClient):
    """ Abstract PosgreSQL client factory """
    pg_client = client(loop, conf)
    pg = await pg_client.connect(loop, conf)
    return pg
