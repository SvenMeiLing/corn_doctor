# -*- coding: utf-8 -*-
# FileName: get_current_user.py
# Time : 2024/6/17 7:28
# Author: zzy
from typing import Annotated, Type

import jwt
from fastapi import HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_403_FORBIDDEN

from app.apis.deps.get_db import get_db
from app.core import config
from app.models.user import UserOrm
from app.schemas.token import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(
        session: Annotated[AsyncSession, Depends(get_db)],
        token: str = Security(reusable_oauth2)
) -> Type[UserOrm]:
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
