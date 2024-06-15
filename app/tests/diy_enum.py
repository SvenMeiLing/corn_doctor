# 定义健康状态的映射
from typing import Literal

from pydantic import BaseModel, model_validator, Field, field_validator

HEALTH_STATUS_MAP = {
    1: "良好",
    2: "一般",
    3: "严重"
}

# 反向映射用于从字符串到整数的转换
HEALTH_STATUS_REVERSE_MAP = {v: k for k, v in HEALTH_STATUS_MAP.items()}


class Model(BaseModel):
    health: Literal["良好", "一般", "严重"] = Field(None, title="健康程度", description="1健康 2轻微 3严重")

    @field_validator("health")
    @classmethod
    def convert_health_to_key(cls, v):
        print(v, "---")
        if v in HEALTH_STATUS_REVERSE_MAP:
            v = HEALTH_STATUS_REVERSE_MAP[v]
            return v
        return v


a = Model(health="一般")
print(a.dict())
