# -*- coding: utf-8 -*-
# FileName: session.py
# Time : 2024/6/12 9:57
# Author: zzy
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from app.core.config import SQLALCHEMY_DATABASE_URI

"""
async with async_engine.connect() as conn:  # 仅仅是个连接
    result = await conn.execute(select(user_table))
    

async with async_engine.begin() as conn:  # 这是一个事务, 在一个事务中可以多次操作
    await conn.execute(
        text("insert into table (x, y, z) values (1, 2, 3)")
    )
    await conn.execute(text("my_special_procedure(7)"))
"""
# 用于连接数据库(当调用时直接启动一个数据库连接,用于直接操作例如建表,改表结构,而非ORM)
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    # connect_args={
    #     'timezone': 'Asia/Shanghai'  # 在连接时设置时区
    # },
    echo=False,  # 打印日志
    echo_pool=False,
    pool_size=10,  # 在连接池中保持打开的连接数
    max_overflow=10,  # 最大连接数
    pool_recycle=1800,  # 表示30分钟后回收连接
    poolclass=AsyncAdaptedQueuePool,  # 异步队列复用连接
)
# 用于与数据库建立会话(使用场景是ORM, 详细见sa.seven.txt)
AsyncSessionFactory = async_sessionmaker(async_engine, expire_on_commit=False, autoflush=False)
