# -*- coding: utf-8 -*-
# FileName: disease.py
# Time : 2024/6/13 20:52
# Author: zzy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.plant import DiseaseOrm


class DiseaseCRUD(CRUDBase):

    async def add_disease_by_name(self, session: AsyncSession, names):
        async for name in names:
            disease = await session.execute(select(DiseaseOrm).where(self.model.name == name))
        return disease

disease_crud = DiseaseCRUD(DiseaseOrm)
