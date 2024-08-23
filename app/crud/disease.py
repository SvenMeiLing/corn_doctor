# -*- coding: utf-8 -*-
# FileName: disease.py
# Time : 2024/6/13 20:52
# Author: zzy
from sqlalchemy import func, select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.plant import DiseaseOrm, plant_disease_association_table


class DiseaseCrud(CRUDBase):
    async def get_ranking(self, async_session: AsyncSession):
        """获取病害排名"""

        stmt = select(
            self.model.name, func.count(plant_disease_association_table.c.disease_id).label("count")
        ).outerjoin(
            plant_disease_association_table, self.model.id == plant_disease_association_table.c.disease_id
        ).group_by(self.model.name).order_by(desc("count"))
        result = await db_session.execute(stmt)
        return result.fetchall()


disease_crud = DiseaseCrud(DiseaseOrm)
