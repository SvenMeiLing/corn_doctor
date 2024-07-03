# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:08
# Author: zzy
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase, CreateSchemaType
from app.db.session import AsyncSessionFactory
from app.models.plant import PlantOrm, DiseaseOrm
from app.schemas.plant import PlantCreate


class PlantCRUD(CRUDBase):

    async def add_plant(self, session: AsyncSession, *, obj_in: CreateSchemaType):
        # 查找出所有对应病害对象
        result = await session.execute(
            select(DiseaseOrm).filter(DiseaseOrm.name.in_(obj_in.diseases))
        )
        # 移除原有diseases值
        plant_obj_in = obj_in.dict(exclude={"diseases"})
        # 修改diseases值
        plant_obj = self.model(**plant_obj_in, diseases=result.scalars().all())
        session.add(plant_obj)
        await session.commit()
        return plant_obj

        # [{'id': 13, 'name': '玉米叶斑病', 'impact': 1, 'description': '玉米叶斑病是一种由真菌引起的病害，主要在玉米植株的叶片上形成斑点，严重影响玉米的生长和产量。', 'symptom': '病害初期在玉米叶片上出现小圆形或不规则形的灰白色斑点，后期斑点扩展并融合成大片，叶片逐渐枯黄、干枯。', 'cause': '玉米叶斑病主要由真菌类病原体引起，如玉米斑枯病菌（Setosphaeria turcica）。这些病原体侵入玉米植株后，在适宜的环境条件下（如高湿度和适中温度）迅速繁殖。', 'preventive_measure': '1. 使用抗病性强的品种，并定期更换种子。\n2. 确保田间通风良好，及时清除田间杂草。\n3. 采用轮作种植制度，减少病害发生的可能性。\n4. 合理施肥和管理，保持玉米植株的健康状态。\n5. 如发现病害，及时采取化学防治或生物防治措施，避免病害扩散。'}]


plant_crud = PlantCRUD(PlantOrm)

if __name__ == '__main__':
    asyncio.run(plant_crud.add_plant(
        AsyncSessionFactory(),
        obj_in=PlantCreate(
            name="玉米", planting_location="南宁", media_url="yumi.png", health="一般",
            growth="一般", description="又大又甜的玉米", user_id=1, diseases=["玉米叶斑病"]
        ))
    )
