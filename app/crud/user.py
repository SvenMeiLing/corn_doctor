# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/13 19:56
# Author: zzy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import UserOrm
from app.utils.security import verify_password


class UserCrud(CRUDBase):
    """
    对用户态操作做一些封装
    """

    async def get_user_by_username(self, async_session: AsyncSession, username: str) -> UserOrm | None:
        session_user = await async_session.execute(
            select(self.model).where(self.model.username == username)
        )
        return session_user.scalars().first()

    async def authenticate(self, async_session: AsyncSession, username: str, password: str) -> UserOrm | None:
        db_user = await self.get_user_by_username(async_session=async_session, username=username)
        if not db_user:
            return None
        if not verify_password(password, db_user.password):
            return None
        return db_user


user_crud = UserCrud(UserOrm)
