# -*- coding: utf-8 -*-
# FileName: session.py
# Time : 2024/6/12 9:57
# Author: zzy

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

engine = create_async_engine(
    "mysql+aiomysql://root:168168956@127.0.0.1:3306/fast_corn",
    echo=True,  # 打印日志
    pool_size=10,  # 在连接池中保持打开的连接数
    max_overflow=10,  # 最大连接数
    pool_recycle=1800  # 表示30分钟后回收连接
)
Session = async_sessionmaker(engine)
