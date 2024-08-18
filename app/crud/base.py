# -*- coding: utf-8 -*-
# FileName: base.py
# Time : 2024/6/13 9:09
# Author: zzy
# -*- coding: utf-8 -*-
# FileName: base.py
# Time : 2023/8/3 16:32
# Author: zzy
import asyncio
from typing import (
    Any, Dict,
    Generic, Optional, Type,
    TypeVar, Union, Sequence
)

from pydantic import BaseModel
from sqlalchemy import select, Row, RowMapping, extract, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only, joinedload, defer

from app.apis.deps.get_db import get_db
from app.db.base import BaseOrmTable
from app.db.session import async_engine
from app.models.plant import DiseaseOrm, PlantOrm
from app.schemas.user import UserCreate
from app.utils.security import hash_password

ModelType = TypeVar("ModelType", bound=BaseOrmTable)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    这里我们定义了一个泛型类, 允许的类型 -> [
        ModelType, CreateSchemaType, UpdateSchemaType
    ]
    分别是一个用于数据库的sqlalchemy模型类 -> ModelType
    一个用于 新建用户/更新用户 的pydantic模型类 -> ModelType / UpdateSchemaType
    """

    def __init__(self, model: Type[ModelType]):
        """
        默认方法: create - select - update - delete

        * `model`: 一个`sqlalchemy base` 类
        * `schema`: 一个 `pydantic` 模型 / 类
        """
        self.model = model

    async def get(self, async_session: AsyncSession, _id: Any) -> Optional[ModelType]:
        result = await async_session.execute(select(self.model).where(self.model.id == _id))
        # 如果是sa2.0的asyncOrm情况下显式指定 -> selectinload(UserOrm.plants)
        # 可以独立调用此方法selectinload().lazyload(PlantOrm.diseases) -> 仅适用于关系(一对多,多对多)字段
        return result.scalars().first()

    async def get_with_relations(
            self,
            async_session: AsyncSession,
            _id: int,
            *relationship_fields: str
    ) -> Optional[ModelType]:
        """
        获取该模型的所有关系字段, 此方法可重载
        :param async_session: 会话
        :param _id: 主键
        :param relationship_fields: 字段名称
        :return:
        """
        result = await async_session.execute(
            select(self.model)
            .where(self.model.id == _id)
            .options(
                *[selectinload(getattr(self.model, rf)) for rf in relationship_fields]
            )
        )
        return result.scalars().first()

    async def get_multi_with_relations(
            self,
            async_session: AsyncSession,
            *relationship_fields: str
    ) -> Sequence[Row[Any] | RowMapping | Any]:
        """
        获取该模型的所有关系字段, 此方法可重载
        :param async_session: 会话
        :param relationship_fields: 字段名称
        :return:
        """
        stmt = select(self.model).options(
            selectinload(self.model.diseases).load_only(DiseaseOrm.name)
        ).options(load_only(self.model.name, self.model.created_at)).group_by(self.model.created_at)
        # --------------------------------------------------------------
        result = await async_session.execute(stmt)
        data = result.scalars().all()
        # 确保所有属性在此处都已经加载，避免在打印时触发延迟加载
        loaded_data = [
            {
                "name": item.name,
                "diseases": [disease.name for disease in item.diseases]
            }
            for item in data
        ]

        print(loaded_data)
        return data

    async def get_multi(
            self, async_session: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> Sequence[Row | RowMapping | Any]:
        result = await async_session.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def create(self, async_session: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        updated_obj = obj_in.model_copy(update={"password": hash_password(obj_in.password)})
        db_obj = self.model(**updated_obj.dict())
        async_session.add(db_obj)
        await async_session.commit()
        return db_obj
        # result = await async_session.scalars(
        #     select(self.model).options(selectinload(self.model.plants))
        # )
        # # 这边涉及到关系的不能直接返回,而是关系查询后返回,独自更改扩展类即可
        # return result.first()

    async def update(
            self,
            async_session: AsyncSession,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        通过接收用户请求更新字段, 查找当前用户后按照用户提供字段做变更
        :param async_session: 会话
        :param db_obj: 当前用户old
        :param obj_in: 用户提供更新字段new
        :return:
        """
        result = await async_session.execute(select(self.model).where(self.model.id == db_obj.id))
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
            print(update_data)
        user = result.scalars().first()

        for field, val in update_data.items():
            setattr(user, field, val)

        await async_session.commit()
        return user

    async def remove(self, async_session: AsyncSession, *, _id: int) -> None:
        stmt = await async_session.execute(select(self.model).where(self.model.id == _id))
        result = stmt.scalar_one()
        user = await async_session.delete(
            result
        )
        await async_session.flush()
        await async_session.commit()


async def main():
    from app.db.session import AsyncSessionFactory

    from app.db.session import async_engine

    async with AsyncSessionFactory() as session:
        crud_plant = CRUDBase(PlantOrm)
        data = await crud_plant.get_multi_with_relations(session, 'x')
        print(data)

    #     crud_plant = CRUDBase(PlantOrm)
    #     data = await crud_plant.get_multi_with_relations(session, 'x')
    #     return data


if __name__ == '__main__':
    asyncio.run(main())
