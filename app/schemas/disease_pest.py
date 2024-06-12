# -*- coding: utf-8 -*-
# FileName: disease_pest.py
# Time : 2024/6/12 16:57
# Author: zzy
import enum
from typing import List

from pydantic import BaseModel, ConfigDict, Field

# from app.schemas.plant import Plant


class ImpactEnum(enum.Enum):
    HIGH: 1
    MID: 2
    LOW: 3


class Disease(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    name: str = Field(..., max_length=24, title="病害名称")
    impact: ImpactEnum = Field(None, title="影响程度")
    description: str = Field("暂时不明", max_length=512, title="病害描述")
    symptom: str = Field('暂时不明', max_length=256, title="发病特征")
    cause: str = Field("暂时不明", max_length=256, title="病害主因")
    preventive_measure: str = Field("暂无应对策略", max_length=512, title="防治手段")
    plants: List["Plant"] = Field([], description="患此病害的植株")


class Pest(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    name: str = Field(..., max_length=24, title="虫害名称")
    impact: ImpactEnum = Field(None, title="影响程度")
    description: str = Field("暂时不明", max_length=512, title="虫害描述")
    preventive_measure: str = Field("暂无应对策略", max_length=512, title="防治手段")
    plants: List["Plant"] = Field([], description="患此病害的植株")
