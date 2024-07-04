# -*- coding: utf-8 -*-
# FileName: pest.py
# Time : 2024/7/4 15:25
# Author: zzy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.pest import pest_crud
from app.schemas.disease_pest import PestBase, Pest, PestInDBBase

router = APIRouter(prefix="/pest")


@router.get("/", response_model=Pest)
async def get_pest(
        pest_id: int, db_session: AsyncSession = Depends(get_db)
):
    """通过id查询虫害"""
    pest = await pest_crud.get(db_session, pest_id)
    if not pest:
        raise HTTPException(status_code=404, detail="pest not found")
    return pest


@router.get("/plants", response_model=PestInDBBase)
async def get_pest(
        pest_id: int, db_session: AsyncSession = Depends(get_db)
):
    """通过id查询虫害,包括患此病害的植物"""
    pest = await pest_crud.get_with_relations(db_session, pest_id, "plants")
    if not pest:
        raise HTTPException(status_code=404, detail="pest not found")
    return pest


@router.post("/", response_model=Pest)
async def create_pest(
        pest_in: PestBase, db_session: AsyncSession = Depends(get_db)
):
    """新增虫害"""
    pest = await pest_crud.create(db_session, obj_in=pest_in)
    return pest
