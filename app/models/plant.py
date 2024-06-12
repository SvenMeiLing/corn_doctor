# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/12 11:04
# Author: zzy
from sqlalchemy import text
from sqlalchemy import Table, ForeignKey, Column, String
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseOrmTable, TimestampColumns

# 中间表，用于表示多对多关系
plant_disease_association_table = Table(
    'plant_disease',
    BaseOrmTable.metadata,
    Column('plant_id', ForeignKey('plant.id', ondelete="CASCADE"), primary_key=True),
    Column('disease_id', ForeignKey('disease.id', ondelete="CASCADE"), primary_key=True)
)
plant_pest_association_table = Table(
    'plant_pest',
    BaseOrmTable.metadata,
    Column('plant_id', ForeignKey('plant.id', ondelete="CASCADE"), primary_key=True),
    Column('pest_id', ForeignKey('pest.id', ondelete="CASCADE"), primary_key=True)
)


class PlantOrm(BaseOrmTable, TimestampColumns):
    """
    用Tinyint / Integer 作为保存 enum对象数值的字段类型， 而不是用数据库中提供的ENUM类型字段，因为有更好的扩展性，性能，节省空间作为使用理由
    """
    __tablename__ = 'plant'
    __table_args__ = {'comment': '存储用户上传的信息'}

    name: Mapped[str] = mapped_column(String(24), nullable=False, comment='植物名称')
    planting_location: Mapped[str] = mapped_column(String(32), nullable=False, comment='种植地点')
    media_url: Mapped[str | None] = mapped_column(String(256), nullable=True, comment='媒体资源地址')

    _health_status = [(1, "健康"), (2, "轻微病害"), (3, "严重病害")]
    _growth_status = [(1, "茂盛"), (2, "一般"), (3, "枯萎")]
    # server_default -> 数据库级别默认值
    health: Mapped[int] = mapped_column(
        TINYINT, server_default=text("1"), nullable=False,
        comment='植物健康分级 1健康 2轻微病害 3严重病害'
    )
    growth: Mapped[int] = mapped_column(TINYINT, nullable=False, comment='植物生长情况 1茂盛 2一般 3枯萎')
    description: Mapped[str] = mapped_column(String(256), nullable=False, comment='植物的描述信息')

    # 设置外键关联, 每个用户对应多种植株
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', comment="外键与用户表关联", ondelete='CASCADE'), nullable=False)
    # 设置关系, 映射到User.plants字段
    user: Mapped['UserOrm'] = relationship('UserOrm', back_populates='plants')
    # 映射到Disease.plants字段
    diseases: Mapped[list['DiseaseOrm']] = relationship('DiseaseOrm', secondary=plant_disease_association_table,
                                                     back_populates='plants')
    # 映射到Pest.plants字段
    pests: Mapped[list['PestOrm']] = relationship('PestOrm', secondary=plant_pest_association_table,
                                                  back_populates='plants')

    def __str__(self):
        return self.name


class DiseaseOrm(BaseOrmTable):
    __tablename__ = 'disease'
    __table_args__ = {'comment': '存储玉米的相应病害'}

    name: Mapped[str] = mapped_column(String(24), index=True, unique=True, nullable=False, comment='病害名称')

    _impact_level = [(1, "高"), (2, "中"), (3, "低")]
    impact: Mapped[int] = mapped_column(TINYINT, nullable=False, comment='影响程度 1高 2中 3低')
    description: Mapped[str] = mapped_column(String(512), nullable=False, comment='病害描述')
    symptom: Mapped[str] = mapped_column(String(256), default="暂时不明", comment='发病特征')
    cause: Mapped[str] = mapped_column(String(256), default="暂时不明", comment='病害主因')
    preventive_measure: Mapped[str] = mapped_column(String(512), default="暂无应对策略", comment='防治手段')

    plants: Mapped[list['PlantOrm']] = relationship('PlantOrm', secondary=plant_disease_association_table,
                                               back_populates='diseases')

    def __str__(self):
        return self.name


class PestOrm(BaseOrmTable):
    __tablename__ = 'pest'
    __table_args__ = {'comment': '存储玉米相关虫害'}

    name: Mapped[str] = mapped_column(String(24), unique=True, nullable=False, comment='虫害种类名称')

    _impact_level = [(1, "高"), (2, "中"), (3, "低")]
    impact: Mapped[int] = mapped_column(TINYINT, nullable=False, comment='影响程度 1高 2中 3低')
    description: Mapped[str] = mapped_column(String(512), nullable=False, comment='虫害描述')
    preventive_measures: Mapped[str] = mapped_column(String(512), default="暂无应对策略", comment='防治手段')

    plants: Mapped[list['PlantOrm']] = relationship('PlantOrm', secondary=plant_pest_association_table, back_populates='pests')

    def __str__(self):
        return self.name
