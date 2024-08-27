# -*- coding: utf-8 -*-
# FileName: hd_redis.py
# Time : 2024/8/22 22:47
# Author: zzy
import os
import time

import aioredis
from aioredis import Redis, ConnectionPool


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


async def hd_redis(id_):
    redis = aioredis.Redis(
        connection_pool=ConnectionPool(
            max_connections=os.cpu_count() * 2
        )
    )
    res = await redis.set("name", "zzy")
    print(id_)


def sync_redis(id_):
    asyncio.run(hd_redis(id_))


if __name__ == '__main__':
    import asyncio


    async def main():
        redis = await get_redis_connection()

        await record_disease(redis, "玉米叶斑病", 100)
        await record_disease(redis, "玉米锈病", 90)
        await record_disease(redis, "玉米叶枯病", 12)
        await record_disease(redis, "玉米条纹病", 12)
        await record_disease(redis, "玉米灰斑病", 12)

        top_diseases = await get_top_diseases(redis, -1)
        print(top_diseases)

        await redis.close()


    async def main2():
        await asyncio.gather(
            *[hd_redis(_) for _ in range(990)]
        )


    s = time.time()
    asyncio.run(main())
    print(time.time() - s)
