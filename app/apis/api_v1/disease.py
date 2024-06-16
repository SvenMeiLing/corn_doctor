# -*- coding: utf-8 -*-
# FileName: disease.py
# Time : 2024/6/13 20:52
# Author: zzy

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.disease import disease_crud
from app.schemas.disease_pest import Disease

router = APIRouter(prefix="/disease")


@router.get("/", response_model=Disease)
async def get_disease(
        disease_id: int, db_session: AsyncSession = Depends(get_db)
):
    disease = await disease_crud.get(db_session, disease_id)
    return disease


@router.post("/", response_model=Disease)
async def create_disease(
        disease_in: Disease, db_session: AsyncSession = Depends(get_db)
):
    disease = await disease_crud.create(db_session, obj_in=disease_in)
    return disease
