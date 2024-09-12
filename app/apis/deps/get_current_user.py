# -*- coding: utf-8 -*-
# FileName: get_current_user.py
# Time : 2024/6/17 7:28
# Author: zzy
from typing import Annotated, Type

import jwt
from aioredis import Redis
from fastapi import HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError, ExpiredSignatureError
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
    redis: Redis = request.app.state.redis
    # 检查是否存在与黑名单
    is_blacklisted = await check_blacklist(redis, token)
    if is_blacklisted:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Your token has been revoked! Please log in again"
        )

    try:
        payload = jwt.decode(
            token, config.SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

    except ExpiredSignatureError:  # 过期错误
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="The token has expired"
        )
    except PyJWTError:  # 其他错误(无效token, 签名错误等)
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

    user = await session.get(UserOrm, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


async def token_revoking(
        redis: Redis, token: str
):
    # 将 token 添加到集合中
    await redis.sadd(config.BLACKLISTED_TOKENS, token)
    # 设置过期时间
    await redis.expire(config.BLACKLISTED_TOKENS, config.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 关闭 Redis 连接
    await redis.close()


async def check_blacklist(
        redis: Redis, token: str
):
    # 检查 token 是否在集合中
    is_member = await redis.sismember(config.BLACKLISTED_TOKENS, token)
    await redis.close()
    return is_member


def get_current_active_user(current_user: UserOrm = Security(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


CurrentUser = Annotated[UserOrm, Depends(get_current_user)]


def get_current_active_superuser(current_user: CurrentUser) -> UserOrm:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
# todo: 如何解决redis jwt重传问题?
# todo: 如何解决jwt吊销问题(黑名单, 短期)
# 在创建一个token时去get是否存在, 如果存在则不创建
# key的改变 -> user:1
# 如果已经存在一个token, 则吊销它新建一个
# 可能我调用此函数的方式有两种(1.orm层面 2.视图层), 于是作此注解
