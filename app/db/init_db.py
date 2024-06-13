# -*- coding: utf-8 -*-
# FileName: init_db.py
# Time : 2024/6/12 10:26
# Author: zzy
import asyncio

from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.db.session import AsyncSessionFactory, async_engine
from app.models.user import UserOrm

"""
如果使用engine.begin(),就必须使用engine.dispose关闭
"""


# async def create_tables():
#     # 根据映射创建表
#     async with async_engine.begin() as conn:
#         from app.db.base import BaseOrmTable
#         # 由于create_all方法会涉及到一些同步操作, 所以使用同步方式包装此方法
#         await conn.run_sync(BaseOrmTable.metadata.create_all)
#     await async_engine.dispose()  # 此处需要显示关闭不然会报错RuntimeError: Event loop is closed


async def main():
    print("开始建立表...")
    # 根据映射创建表
    # 根据映射创建表
    async with async_engine.begin() as conn:
        from app.db.base import BaseOrmTable
        # 由于create_all方法会涉及到一些同步操作, 所以使用同步方式包装此方法
        await conn.run_sync(BaseOrmTable.metadata.create_all)

    print("结束建立表...")

    async with AsyncSessionFactory() as session:  # 创建并管理会话
        async with session.begin():  # 创建并管理事务
            # 添加用户
            new_user = UserCreate(username="xax", password=hash_password("xxx"))
            user_obj = UserOrm(**new_user.dict())
            session.add_all([user_obj, user_obj, user_obj])
            print(user_obj.__dict__)
            await session.flush()  # 预提交
            # await session.commit()
        # await session.close()  # 关闭会话

    await async_engine.dispose()  # 此处需要显示关闭不然会报错RuntimeError: Event loop is closed


if __name__ == '__main__':
    # 运行主函数
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # ------------------------------
    asyncio.run(main())
