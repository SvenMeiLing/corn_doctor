# -*- coding: utf-8 -*-
# FileName: main.py
# Time : 2024/6/13 20:01
# Author: zzy
from fastapi import FastAPI
from app.apis.api_v1.user import router as user_router
from app.apis.api_v1.disease import router as disease_router
from app.apis.api_v1.plant import router as plant_router

app = FastAPI()
app.include_router(user_router)
app.include_router(disease_router)
app.include_router(plant_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
