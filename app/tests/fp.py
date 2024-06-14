from fastapi import FastAPI, HTTPException
from enum import Enum, IntEnum


# 定义枚举类
class ModelName(IntEnum):
    alexnet = "1"
    resnet = "2"
    lenet = "3"


# 创建FastAPI实例
app = FastAPI()


# 创建GET接口
@app.get("/model/{model_id}")
async def get_model_name(model_name: ModelName):
    try:
        # 根据输入的整数值返回相应的枚举名称
        print(model_name.value)
        model_name = ModelName(model_name).name
        return {"model_id": model_name, "model_name": model_name}
    except ValueError:
        # 如果输入值不在枚举范围内，抛出HTTP 400错误
        raise HTTPException(status_code=400, detail="Invalid model ID. Valid IDs are 1, 2, 3.")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
