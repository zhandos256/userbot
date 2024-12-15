import aioredis

redis = aioredis.from_url('redis://localhost:6379')


async def set_cache(key: str, value: str, expire: int = 3600):
    await redis.set(name=key, value=value, ex=expire)


async def get_cache(key: str):
    await redis.get(name=key)