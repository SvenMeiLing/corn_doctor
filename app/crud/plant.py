# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/13 21:08
# Author: zzy
import asyncio
from datetime import timedelta, datetime
from typing import Literal, Sequence, Any

from sqlalchemy import (
    func, select, extract, case, Row, RowMapping, and_, true
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.crud.base import CreateSchemaType
from app.db.session import AsyncSessionFactory
from app.models.plant import DiseaseOrm, plant_disease_association_table
from app.models.plant import PlantOrm
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

    async def get_multi_with_relations(
            self,
            async_session: AsyncSession,
            mode: Literal["year", "month", "day"]
    ) -> Sequence[Row[Any] | RowMapping | Any]:
        """
        获取该模型的所有关系字段, 此方法可重载
        :param mode: 按年月日其一分组做分组查询
        :param async_session: 会话
        :return:
        """
        # stmt = select(self.model).options(
        #     selectinload(self.model.diseases).load_only(DiseaseOrm.name)
        # ).options(load_only(self.model.name, self.model.created_at)).group_by(self.model.created_at)
        # --------------------------------------------------------------
        # stmt2 = select(
        #     extract(mode, self.model.created_at).label(mode),
        #     DiseaseOrm.name.label('dis_name'),
        #     func.count(self.model.id).label('total')
        # ).join(plant_disease_association_table, self.model.id == plant_disease_association_table.c.plant_id). \
        #     join(DiseaseOrm, DiseaseOrm.id == plant_disease_association_table.c.disease_id). \
        #     group_by(mode, DiseaseOrm.name). \
        #     order_by(mode, DiseaseOrm.name)
        # ----------------------------------------------------------------
        # 获取上周的开始和结束日期
        today = datetime.today()
        # 获取上周一的时间差
        last_monday = today - timedelta(days=today.weekday() + 7)
        # 计算上周日时间
        last_sunday = last_monday + timedelta(days=6)

        # 构造select
        select_ = None
        # 如果mode为周参数需要特殊处理
        if mode == "week":
            select_ = select(
                case(
                    (func.dayofweek(self.model.created_at) == 1, '周一'),
                    (func.dayofweek(self.model.created_at) == 2, '周二'),
                    (func.dayofweek(self.model.created_at) == 3, '周三'),
                    (func.dayofweek(self.model.created_at) == 4, '周四'),
                    (func.dayofweek(self.model.created_at) == 5, '周五'),
                    (func.dayofweek(self.model.created_at) == 6, '周六'),
                    (func.dayofweek(self.model.created_at) == 7, '周天'),
                    else_='Unknown'
                ).label(mode),
                DiseaseOrm.name.label(mode),
                func.count(self.model.id).label('total')
            )
        else:  # 处理year和month的逻辑
            select_ = select(
                func.concat(
                    extract(mode, self.model.created_at),
                    "年" if mode == "year" else "月"
                ).label(mode),
                DiseaseOrm.name.label(mode),
                func.count(self.model.id).label('total')
            )
        stmt2 = select_.join(
            plant_disease_association_table, self.model.id == plant_disease_association_table.c.plant_id
        ).join(
            DiseaseOrm, DiseaseOrm.id == plant_disease_association_table.c.disease_id
        ).where(
            and_(
                self.model.created_at >= last_monday,
                self.model.created_at <= last_sunday
            ) if mode == "week" else true()  # 如果不是week参数,直接放行这个where
        ).group_by(mode, DiseaseOrm.name) \
            .order_by(mode, DiseaseOrm.name)
        result = await async_session.execute(stmt2)
        # 确保所有属性在此处都已经加载，避免在打印时触发延迟加载
        return result.all()


plant_crud = PlantCRUD(PlantOrm)

if __name__ == '__main__':
    # asyncio.run(plant_crud.add_plant(
    #     AsyncSessionFactory(),
    #     obj_in=PlantCreate(
    #         name="玉米", planting_location="南宁", media_url="yumi.png", health="一般",
    #         growth="一般", description="又大又甜的玉米", user_id=1, diseases=["玉米叶斑病"]
    #     ))
    # )
    res = asyncio.run(plant_crud.get_multi_with_relations(
        AsyncSessionFactory(),
        "year"
    ))
    print(res)
