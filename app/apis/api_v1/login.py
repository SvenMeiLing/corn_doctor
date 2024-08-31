# -*- coding: utf-8 -*-
# FileName: login.py
# Time : 2024/6/17 11:45
# Author: zzy
import json
from datetime import timedelta
from typing import Annotated

from aioredis import Redis
from fastapi import APIRouter, Depends, HTTPException, Response, Security
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request

from app.apis.deps.get_current_user import get_current_user, reusable_oauth2
from app.apis.deps.get_db import get_db
from app.core import config
from app.crud.user import user_crud
from app.models.user import UserOrm
from app.schemas.token import Token
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserBase
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
    user = await user_crud.authenticate(async_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="错误的用户名或密码")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    # 生成token
    token = Token(
        access_token=security.create_access_token(user.id, expires_delta=access_token_expires)
    )
    # 存入缓存
    redis: Redis = request.app.state.redis
    user_dict = UserBase(**user.to_dict()).model_dump_json()
    await redis.set(f"{config.JWT_PREFIX}:{token.access_token}", json.dumps(user_dict))
    return token


@router.get("/logout")
async def logout(
        request: Request,
        current_user: Annotated[dict | UserBase, Depends(get_current_user)],
        token: str = Security(reusable_oauth2)
):
    redis: Redis = request.app.state.redis
    await redis.delete(f"{config.JWT_PREFIX}:{token}")
    return Response("success")
