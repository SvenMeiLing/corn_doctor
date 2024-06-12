# -*- coding: utf-8 -*-
# FileName: init_db.py
# Time : 2024/6/12 10:26
# Author: zzy
import asyncio

from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.db.session import engine, Session
from app.models.user import UserOrm


async def create_tables():
    # 根据映射创建表
    async with engine.begin() as conn:
        from app.db.base import BaseOrmTable
        # 由于create_all方法会涉及到一些同步操作, 所以使用同步方式包装此方法
        await conn.run_sync(BaseOrmTable.metadata.create_all)


async def main():
    print("开始建立表...")
    await create_tables()
    print("结束建立表...")

    async with Session.begin() as session:
        # 添加用户
        new_user = UserCreate(username="zzy", password=hash_password("168168956"))
        user_obj = UserOrm(**new_user.dict())
        session.add(user_obj)
        await session.flush()
        print(user_obj.__dict__)
        await session.close()


if __name__ == '__main__':
    # 运行主函数
    asyncio.run(main())
