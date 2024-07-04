# -*- coding: utf-8 -*-
# FileName: main.py
# Time : 2024/6/13 20:01
# Author: zzy
from fastapi import FastAPI, APIRouter
from starlette.staticfiles import StaticFiles

from app.apis.api_v1.user import router as user_router
from app.apis.api_v1.disease import router as disease_router
from app.apis.api_v1.pest import router as pest_router
from app.apis.api_v1.plant import router as plant_router
from app.core.config import PREDICT_PATH

API_VERSION = "/api/v1"

app = FastAPI()
v1 = APIRouter(prefix=API_VERSION)

v1.include_router(user_router, tags=["user"])
v1.include_router(disease_router, tags=["disease"])
v1.include_router(pest_router, tags=["pest"])
v1.include_router(plant_router, tags=["plant"])

app.include_router(v1)

# 挂载静态文件目录到 /predict 路由
app.mount("/predict", StaticFiles(directory=PREDICT_PATH), name="predict")
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
