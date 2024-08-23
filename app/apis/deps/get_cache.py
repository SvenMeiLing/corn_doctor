# -*- coding: utf-8 -*-
# FileName: get_cache.py
# Time : 2024/8/23 21:04
# Author: zzy

async def get_cache():
    print("get_cache")
    from main import redis_pool
    print(redis_pool, "<----")
    try:
        yield redis_pool
    finally:
        redis_pool.close()
