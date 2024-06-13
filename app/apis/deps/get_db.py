# -*- coding: utf-8 -*-
# FileName: get_db.py
# Time : 2024/6/13 10:11
# Author: zzy
# Dependency
from typing import AsyncGenerator

from app.db.session import AsyncSessionFactory


# Dependency
async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
