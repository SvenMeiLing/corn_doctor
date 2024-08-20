# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:06
# Author: zzy
from pathlib import Path
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.apis.deps.get_db import get_db
from app.core.config import ORIGIN_IMG_PATH, MEDIA_ROOT, PREDICT_PATH
from app.crud.plant import plant_crud
from app.schemas.plant import Plant, PlantCreate, PlantDiseaseTotal
from app.utils.group_by import group_by_date
from app.utils.hasher import gen_hashed, gen_file_path
from app.vision.yolo_predict import yolo

router = APIRouter(prefix="/plant")


@router.get("/", response_model=Plant)
async def get_plant(
        plant_id: int, db_session: AsyncSession = Depends(get_db)
):
    plant = await plant_crud.get_with_relations(db_session, plant_id, "diseases", "pests")
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


# todo: (当日,月度,季度,年度病害排行)
#  /plant/disease_visualization
"""
data: [
    玉米叶斑病:[
        2024-07-18, 
    ]
]
"""


@router.get("/disease_visualization")
async def disease_visualization(
        db_session: AsyncSession = Depends(get_db),
        *,
        mode: Literal["year", "month", "week", "day"]
):
    plant = await plant_crud.get_multi_with_relations(db_session, mode)

    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    grouped = group_by_date(plant, mode)
    return grouped


@router.post("/yolo_identify", response_model=list[Plant])
async def yolo_identify(
        files: list[UploadFile], db_session: AsyncSession = Depends(get_db)
):
    """
    todo:用户上传多张图片, 存储原图并且识别后保存预测结果图片, 存储到数据库,
        用户通过url访问预测结果图片, 例如:xxx.png -> http://127.0.0.1:8000/predict/2024/07/02/xx.png
        数据库层面 -> 使用/predict/2024/07/02/xx.png
        yolo保存层面 -> 使用"http://127.0.0.1:8000" + /predict/2024/07/02/xx.png
        代理predict目录,返回/predict/2024/07/02/xx.png
    """
    result = []
    # 拿到多张图片, 进行保存并生成hash名称, 识别
    for img in files:
        # 读取文件内容并生成hash
        content = await img.read()
        # 哈希后的文件名称
        md5_name = gen_hashed(content) + Path(img.filename).suffix
        # 生成不带前缀的路径
        media_url = gen_file_path(md5_name)
        # 保存文件到指定目录下
        origin_img_path = ORIGIN_IMG_PATH / md5_name

        with open(origin_img_path, "wb") as f:
            f.write(content)

        # [{'玉米灰斑病': 1, '玉米叶枯病': 1}]
        outputs = yolo(PREDICT_PATH / media_url, origin_img_path)

        # 产生每个对象
        pc = PlantCreate(
            name="玉米", planting_location="河南舞阳",
            media_url=MEDIA_ROOT + media_url,  # 生成hash文件名称
            health="一般", growth="一般",
            description="来自河南的用户", user_id=1, diseases=list(outputs[0])
        )
        plant_obj = await plant_crud.add_plant(db_session, obj_in=pc)
        result.append(plant_obj)
    return result
