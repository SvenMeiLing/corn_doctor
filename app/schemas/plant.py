# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/12 13:15
# Author: zzy
import enum
from typing import List

from pydantic import BaseModel, StringConstraints, Field, ConfigDict, FilePath
from typing_extensions import Annotated

from app.schemas.disease_pest import Disease, Pest


class PlantBase(BaseModel):
    class HealthStatus(enum.Enum):
        # 健康状态
        HEALTHY = 1
        MILD_DISEASE = 2
        SEVERE_DISEASE = 3

    class GrowthStatus(enum.Enum):
        # 生长状态
        FLOURISHING = 1
        AVERAGE = 2
        WITHERED = 3

    name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=24)
    ] = Field(None, example="葡萄", title="名称", description="植物名称")
    planting_location: Annotated[str, StringConstraints(strip_whitespace=True, max_length=32)]
    media_url: FilePath = Field(
        None, example="home/media/2024/07/19/dsadjaki1u23iedbai.png", title="图片资源地址",
        description="植株图片存储地址(相对路径)"
    )
    health: HealthStatus | None = Field(None, title="健康程度", description="1健康 2轻微 3严重")
    growth: GrowthStatus | None = Field(None, title="生长程度", description="1茂盛 2一般 3枯萎")
    description: Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=256)
    ] = Field(None, example="这是蓝莓巨峰,酸甜可口", title="描述", description="植物描述信息")


class PlantCreate(PlantBase):
    pass


class PlantUpdate(PlantBase):
    pass


class PlantInDBBase(PlantBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    user_id: int
    diseases: List[Disease] = Field([], title="该植株的所有病害")
    pests: List[Pest] = Field([], title="该植株的所有虫害")


class Plant(PlantBase):
    pass
