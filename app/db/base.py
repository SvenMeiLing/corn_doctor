# -*- coding: utf-8 -*-
# FileName: base.py
# Time : 2024/6/12 8:52
# Author: zzy
from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from sqlalchemy.ext.asyncio import AsyncAttrs


class BaseOrmTable(AsyncAttrs, DeclarativeBase):  # 继承异步属性
    """SQLAlchemy 基本ORM模型类, 可以在此实现一些公共方法"""
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()
    # 设置共同主键, 且sort_order设置为-1表示主键列处于最前
    id: Mapped[int] = mapped_column(primary_key=True, comment="主键", autoincrement=True, sort_order=-1)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self, alias_dict: dict = None, exclude_none=True) -> dict:
        """
        数据库模型转dic
        :param alias_dict: 别名字典 eg: {id:user_id}, 把id别名化
        :param exclude_none: 默认排查None值
        :return: dict
        """
        alias_dict = alias_dict or {}
        if exclude_none:
            return {
                alias_dict.get(c.name, c.name): getattr(self, c.name)
                for c in self.__table__.columns if getattr(self, c.name) is not None
            }
        else:
            return {
                alias_dict.get(c.name, c.name): getattr(self, c.name, None)
                for c in self.__table__.columns
            }


class TimestampColumns(AsyncAttrs, DeclarativeBase):
    """时间戳相关列, 可以由需要此类自字段的表继承便于复用"""
    __abstract__ = True  # 不能实例化, 只能将此抽象类作为基类继承

    created_at: Mapped[datetime] = mapped_column(default=datetime.now, comment="创建时间")

    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, comment="更新时间")

    deleted_at: Mapped[datetime] = mapped_column(nullable=True, comment="删除时间")


"""
An integer that indicates how this mapped column should be sorted compared to the others when the ORM is creating a Table. Among mapped columns that have the same value the default ordering is used, placing first the mapped columns defined in the main class, then the ones in the super classes. Defaults to 0. The sort is ascending.
"""
