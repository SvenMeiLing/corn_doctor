# -*- coding: utf-8 -*-
# FileName: post.py
# Time : 2024/9/12 20:25
# Author: zzy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseOrmTable, TimestampColumns


class PostOrm(BaseOrmTable, TimestampColumns):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(String(32), comment="帖子标题")
    content: Mapped[str] = mapped_column(String(2048), comment="帖子内容")
    images: Mapped[str] = mapped_column(String(256), comment="帖子配图")

