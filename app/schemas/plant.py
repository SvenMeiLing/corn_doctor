# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/12 13:15
# Author: zzy
import enum
from typing import Union
from typing import List, Any

from pydantic import BaseModel, StringConstraints, Field, ConfigDict, field_validator
from typing_extensions import Annotated

from app.models.custom_field import FilePath, FilePathStr


class PlantBase(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

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
    media_url: FilePathStr | str = Field(
        None, example="dsadjaki1u23iedbai.png", title="图片资源地址",
        description="植株图片存储地址(相对路径)"
    )
    health: HealthStatus | None = Field(None, title="健康程度", description="1健康 2轻微 3严重")
    growth: GrowthStatus | None = Field(None, title="生长程度", description="1茂盛 2一般 3枯萎")
    description: Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=256)
    ] = Field(None, example="这是蓝莓巨峰,酸甜可口", title="描述", description="植物描述信息")


# todo: 使用自定义类型解决, 使其支持适应各自输入, 通过我的hook自动转化

class PlantCreate(PlantBase):
    user_id: int


class PlantUpdate(PlantBase):
    pass


class PlantInDBBase(PlantBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    user_id: int
    diseases: List["Disease"] = Field([], title="该植株的所有病害")
    pests: List["Pest"] = Field([], title="该植株的所有虫害")


class Plant(PlantBase):
    pass


from app.schemas.disease_pest import Disease, Pest

PlantInDBBase.update_forward_refs()

if __name__ == '__main__':
    p = PlantBase(name="pt", planting_location='xy', media_url='xxx.png', health=PlantBase.HealthStatus.HEALTHY,
                  growth=PlantBase.GrowthStatus.FLOURISHING, description='xxx')
    print(p.dict())
