# -*- coding: utf-8 -*-
# FileName: store.py
# Time : 2024/6/28 21:17
# Author: zzy
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.store import store_crud
from app.schemas.store import ProductBase

router = APIRouter(prefix="/plant")


@router.get("/", response_model=List[ProductBase])
async def list_product(
        db_session: AsyncSession = Depends(get_db)
):
    products = await store_crud.get_multi(db_session)
    if not products:
        raise HTTPException(status_code=404, detail="Products is None")
    return products


@router.post("/", response_model=ProductBase)
async def create_plant(
        plant_in: PlantCreate, db_session: AsyncSession = Depends(get_db)
):
    print(plant_in, "<-------------")
    plant_in = await plant_crud.create(db_session, obj_in=plant_in)
    return plant_in
