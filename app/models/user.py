# -*- coding: utf-8 -*-
# FileName: user.py
# Time : 2024/6/12 10:35
# Author: zzy
from sqlalchemy.sql.sqltypes import String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseOrmTable, TimestampColumns
from app.models.plant import PlantOrm


class UserOrm(BaseOrmTable, TimestampColumns):
    """用户表"""
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(String(30), comment="用户名")
    password: Mapped[str] = mapped_column(String(64), comment="密码")
    tel: Mapped[str] = mapped_column(String(11), comment="手机号", nullable=True)
    email: Mapped[str] = mapped_column(String(30), comment="邮箱", nullable=True)
    avatar: Mapped[str] = mapped_column(String(30), comment="头像", nullable=True)

    # 设置关系, 映射到Plant.user字段
    plants: Mapped[list[PlantOrm]] = relationship('PlantOrm', back_populates="user")
