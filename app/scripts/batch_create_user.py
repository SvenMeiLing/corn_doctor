# -*- coding: utf-8 -*-
# FileName: batch_create_user.py
# Time : 2024/8/27 21:15
# Author: zzy
import asyncio
import csv

from faker import Faker

from app.db.session import AsyncSessionFactory
from app.models.user import UserOrm

fake = Faker()


def userinfo_to_csv(pwd_length=9):
    """批量生成用户信息"""
    data = [
        ["username", "password"]
    ]
    data.extend([[fake.user_name(), fake.password(length=pwd_length)] for _ in range(100)])
    with open("user_profile.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


async def insert_to_db():
    with open("user_profile.csv", encoding="utf-8") as f:
        data = list(csv.reader(f))[1:]
        async with AsyncSessionFactory() as session:
            async with session.begin():
                users = [UserOrm(username=user[0], password=user[1]) for user in data]
                session.add_all(users)
                await session.flush()


if __name__ == '__main__':
    asyncio.run(insert_to_db())
