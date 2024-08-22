# -*- coding: utf-8 -*-
# FileName: hd_redis.py
# Time : 2024/8/22 22:47
# Author: zzy
import aioredis
from aioredis import Redis


async def get_redis_connection():
    redis = await aioredis.from_url("redis://localhost")
    return redis


async def record_disease(redis: Redis, disease, count):
    key = "daily_disease_ranking"
    await redis.zadd(key, {disease: count})


async def get_top_diseases(redis: Redis, top_n):
    key = "daily_disease_ranking"
    top_diseases = await redis.zrevrange(key, 0, top_n - 1, withscores=True)
    return {disease.decode(): int(count) for disease, count in top_diseases}


if __name__ == '__main__':
    import asyncio


    async def main():
        redis = await get_redis_connection()

        await record_disease(redis, "blight", 100)
        await record_disease(redis, "rust", 90)
        await record_disease(redis, "smut", 12)
        await record_disease(redis, "霜霉病", 12)

        top_diseases = await get_top_diseases(redis, 4)
        print(top_diseases)

        await redis.close()

    asyncio.run(main())
