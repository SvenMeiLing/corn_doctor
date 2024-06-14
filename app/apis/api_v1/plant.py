# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:06
# Author: zzy

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.plant import plant_crud
from app.schemas.plant import Plant, PlantCreate

router = APIRouter(prefix="/v1/plant")


@router.get("/", response_model=Plant)
async def get_plant(
        plant_id: int, db_session: AsyncSession = Depends(get_db)
):
    plant = await plant_crud.get(db_session, plant_id)
    print(plant.to_dict())
    return plant


@router.post("/", response_model=Plant)
async def create_plant(
        plant_in: PlantCreate, db_session: AsyncSession = Depends(get_db)
):
    print(plant_in, "<-------------")
    plant_in = await plant_crud.create(db_session, obj_in=plant_in)
    return plant_in
