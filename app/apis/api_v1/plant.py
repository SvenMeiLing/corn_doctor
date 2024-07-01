# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:06
# Author: zzy

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.crud.plant import plant_crud
from app.models.plant import PlantOrm
from app.schemas.plant import Plant, PlantCreate
from app.utils.hasher import gen_hashed
from app.vision.yolo_predict import yolo

router = APIRouter(prefix="/plant")


@router.get("/", response_model=Plant)
async def get_plant(
        plant_id: int, db_session: AsyncSession = Depends(get_db)
):
    plant = await plant_crud.get(db_session, plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return plant


@router.post("/", response_model=Plant)
async def create_plant(
        plant_in: PlantCreate, db_session: AsyncSession = Depends(get_db)
):
    print(plant_in, "<-------------")
    plant_in = await plant_crud.create(db_session, obj_in=plant_in)
    return plant_in


@router.post("/yolo_identify", response_model=Plant)
async def yolo_identify(
        plant_imgs: list[UploadFile], db_session: AsyncSession = Depends(get_db)
):
    # 拿到多张图片, 进行保存并生成hash名称, 识别
    for img in plant_imgs:
        # 读取文件内容并生成hash
        content = await img.read()
        gen_hashed(content)
        # 产生每个
        pc = PlantCreate(
            name="玉米", planting_location="河南舞阳",
            media_url=img.filename, health="一般", growth="一般",
            description="来自河南的用户", user_id=1
        )
        plant_crud.create(db_session, obj_in=pc)
