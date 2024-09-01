# -*- coding: utf-8 -*-
# FileName: login.py
# Time : 2024/6/17 11:45
# Author: zzy
from datetime import timedelta
from typing import Annotated

from aioredis import Redis
from fastapi import APIRouter, Depends, HTTPException, Response, Security
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.apis.deps.get_current_user import get_current_user, token_revoking, reusable_oauth2
from app.apis.deps.get_db import get_db
from app.core import config
from app.crud.user import user_crud
from app.models.user import UserOrm
from app.schemas.token import Token
from app.utils import security

router = APIRouter()


@router.post("/login/access-token")
async def login_access_token(
        async_session: AsyncSession = Depends(get_db),
        *,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        request: Request
) -> Token:
    """
    校验用户登录请求,并响应token
    """
    redis: Redis = request.app.state.redis
    user = await user_crud.authenticate(async_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Wrong username or password")
    # 从缓存查询,如果有token直接返回
    token = await redis.get(f"{config.JWT_PREFIX}:{user.id}")
    if token:
        return Token(access_token=token)

    # 如果缓存中不存在直接新建
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

    # 生成token
    token = Token(
        access_token=security.create_access_token(user.id, expires_delta=access_token_expires)
    )
    # 存储用户的token
    await redis.set(f"{config.JWT_PREFIX}:{user.id}", token.access_token, ex=access_token_expires)
    return token


@router.get("/logout")
async def logout(
        request: Request,
        current_user: Annotated[UserOrm, Depends(get_current_user)],
        token: str = Security(reusable_oauth2)
):
    redis: Redis = request.app.state.redis
    # 删除旧的token(用于防止token重传)
    await redis.delete(f"{config.JWT_PREFIX}:{current_user.id}")
    # 吊销token(用于吊销token)
    await token_revoking(redis, token)
    return Response("success")
