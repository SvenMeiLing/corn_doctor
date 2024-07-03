# -*- coding: utf-8 -*-
# FileName: plant.py
# Time : 2024/6/12 13:15
# Author: zzy
from typing import Literal, List

from pydantic import BaseModel, StringConstraints, Field, ConfigDict, field_serializer, field_validator
from typing_extensions import Annotated

from app.models.custom_field import FilePathStr

# 定义健康状态的映射
HEALTH_STATUS_MAP = {
    1: "良好",
    2: "一般",
    3: "较差"
}

# 反向映射用于从字符串到整数的转换
HEALTH_STATUS_REVERSE_MAP = {v: k for k, v in HEALTH_STATUS_MAP.items()}


class PlantBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=False)

    name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=24)  # type: ignore
    ] = Field(None, example="葡萄", title="名称", description="植物名称")
    planting_location: Annotated[str, StringConstraints(strip_whitespace=True, max_length=32)]  # type: ignore
    media_url: str = Field(
        None, example="md5.png", title="图片资源地址",
        description="植株图片存储地址(相对路径)"
    )
    # 由于模型可能会出现映射所以支持literal和int
    health: Literal["良好", "一般", "较差"] | int = Field(None, title="健康程度", description="1健康 2轻微 3严重")
    growth: Literal["良好", "一般", "较差"] | int = Field(None, title="生长程度", description="1茂盛 2一般 3枯萎")
    description: Annotated[
        str,
        StringConstraints(strip_whitespace=True, max_length=256)  # type: ignore
    ] = Field(None, example="这是蓝莓巨峰,酸甜可口", title="描述", description="植物描述信息")

    @field_serializer("health", "growth", when_used="json")  # 响应时调用此方法序列化字段
    def convert(self, key):  # 将此字段的值若为int, 序列化成对于的文字访问, 例如v是从数据库去到的1->映射->良好
        if key in HEALTH_STATUS_MAP:  # 如果key是1返回良好
            return HEALTH_STATUS_MAP[key]
        elif key in HEALTH_STATUS_REVERSE_MAP:  # 如果key是良好返回1
            return HEALTH_STATUS_REVERSE_MAP[key]
        return None

    @field_validator("health", "growth")  # 验证时调用此方法变更字段的值
    @classmethod
    def to_name(cls, key):  # 使用plain, 让字段验证处于序列化钩子中(也就是提供给convert)而不是直接报错
        if key in HEALTH_STATUS_MAP:
            return key
        elif key in HEALTH_STATUS_REVERSE_MAP:  # 如果验证时post给的是良好, 返回1
            return HEALTH_STATUS_REVERSE_MAP[key]
        return 2


# todo: 使用自定义类型解决, 使其支持适应各自输入, 通过我的hook自动转化


class PlantCreate(PlantBase):
    user_id: int

    diseases: List["DiseaseBase"] | List[str] = Field([], title="该植株的所有病害")
    pests: List["Pest"] | List[str] = Field([], title="该植株的所有虫害")


class PlantUpdate(PlantBase):
    pass


class PlantInDBBase(PlantBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    user_id: int
    diseases: List["DiseaseBase"] = Field([], title="该植株的所有病害")
    pests: List["Pest"] = Field([], title="该植株的所有虫害")


class Plant(PlantInDBBase):
    pass


from app.schemas.disease_pest import DiseaseBase, Pest  # type: ignore

PlantInDBBase.update_forward_refs()

if __name__ == '__main__':
    p = PlantBase(
        name="pt", planting_location='xy', media_url='xxx.png', health=HealthEnum.一般,  # type: ignore
        growth=GrowthEnum.一般, description='xxx')  # type: ignore
    print(p.dict())
    # print(p.dict())
