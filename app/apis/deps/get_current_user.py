# -*- coding: utf-8 -*-
# FileName: get_current_user.py
# Time : 2024/6/17 7:28
# Author: zzy
import json
from typing import Annotated, Type

import jwt
from aioredis import Redis
from fastapi import HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from app.apis.deps.get_db import get_db
from app.core import config
from app.models.user import UserOrm
from app.schemas.token import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(
        request: Request,
        session: Annotated[AsyncSession, Depends(get_db)],
        token: str = Security(reusable_oauth2),
) -> Type[UserOrm]:
    """
    匹配出用户传来token
    """
    # 先从缓存中获取用户信息
    userinfo = await get_current_user_toredis(request.app.state.redis, token)
    if userinfo:
        return userinfo
    # 如果缓存没有则走数据库
    try:
        payload = jwt.decode(
            token, config.SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = await session.get(UserOrm, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_user_toredis(
        redis: Redis,
        token: str
):
    # 获取用户信息(名称, id, 头像, 邮箱等)
    userinfo = json.loads(await redis.get(f"{config.JWT_PREFIX}:{token}"))
    return userinfo


def get_current_active_user(current_user: UserOrm = Security(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# 可能我调用此函数的方式有两种(1.orm层面 2.视图层), 于是作此注解
CurrentUser = Annotated[UserOrm, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> UserOrm:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
# todo: 如何解决redis jwt重传问题?
# 尝试去判断这个jwt是否存在
