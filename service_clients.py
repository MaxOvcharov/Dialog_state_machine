import aiopg.sa
import aioredis


class PostgreSQLClient:
    """ PostgreSQL connection pool client """

    def __init__(self, loop, conf):
        self.loop = loop
        self.conf = conf
        self.pg = None

    @classmethod
    async def connect(cls, **options):
        self = cls(**options)
        await self.init_connection()
        return self

    async def init_connection(self):
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


class RedisClient:
    """ Redis connection pool client """

    def __init__(self, loop, conf):
        self.loop = loop
        self.conf = conf
        self.rd = None

    @classmethod
    async def connect(cls, **options):
        self = cls(**options)
        await self.init_connection()
        return self

    async def init_connection(self):
        self.rd = await aioredis.create_pool(
            (self.conf['host'], self.conf['port']),
            db=self.conf['db'],
            password=self.conf['password'],
            maxsize=self.conf['maxsize'],
            minsize=self.conf['minsize'],
            loop=self.conf['loop']
        )

    async def close_connection(self):
        self.rd.close()
        await self.rd.wait_closed()


async def pg_client_factory(loop, conf, client=PostgreSQLClient):
    """ Abstract PosgreSQL client factory """
    pg_client = client(loop, conf)
    pg = await pg_client.connect(loop=loop, conf=conf)
    return pg

async def rd_client_factory(loop, conf, client=RedisClient):
    """ Abstract Redis client factory """
    rd_client = client(loop, conf)
    rd = await rd_client.connect(loop=loop, conf=conf)
    return rd