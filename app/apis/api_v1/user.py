# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/13 19:50
# Author: zzy
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.user import user_crud
from app.schemas.user import UserBase, UserRegister, User

router = APIRouter(prefix="/user")


@router.get("/", response_model=UserBase)
async def get_user(
        user_id: int, db_session: AsyncSession = Depends(get_db)
):
    user = await user_crud.get(db_session, user_id)
    return user


@router.get("/plants", response_model=User)
async def get_user(
        user_id: int, db_session: AsyncSession = Depends(get_db)
):
    user = await user_crud.get_with_relations(db_session, user_id, "plants")
    return user


@router.post("/", response_model=UserBase)
async def create_user(
        user_in: UserRegister, db_session: AsyncSession = Depends(get_db)
):
    user = await user_crud.create(db_session, obj_in=user_in)
    return user
