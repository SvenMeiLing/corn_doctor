from types import DynamicClassAttribute

from fastapi import FastAPI, HTTPException
from enum import Enum, IntEnum

from pydantic import BaseModel, field_validator, field_serializer


# todo: 数据库要在序列化时调用方法使其变为value的值, 而响应用name

# 定义枚举类
class HealthStatus(str, Enum):
    GOOD = 1
    AVERAGE = 2
    POOR = 3

    def __repr__(self):
        return repr(self.name)

    @DynamicClassAttribute
    def name(self) -> str:
        return self._value_

    @DynamicClassAttribute
    def value(self) -> str:
        mapper = {
            "GOOD": "良好",
            "AVERAGE": "一般",
            "POOR": "较差"
        }
        return mapper.get(self._name_, None)


class Model(BaseModel):
    health: HealthStatus

    @field_serializer("health", when_used="json")
    def to_name(self, v):
        return v.value


# 创建FastAPI实例
app = FastAPI()


# 创建GET接口
@app.post("/model/{mn}", response_model=Model)
async def get_model_name(m: Model, mn: HealthStatus):
    try:
        # 根据输入的整数值返回相应的枚举名称
        print(m.dict(), ",<-----")
        return m
    except ValueError:
        # 如果输入值不在枚举范围内，抛出HTTP 400错误
        raise HTTPException(status_code=400, detail="Invalid model ID. Valid IDs are 1, 2, 3.")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
