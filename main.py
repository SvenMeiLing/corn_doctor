# -*- coding: utf-8 -*-
# FileName: main.py
# Time : 2024/6/13 20:01
# Author: zzy
import cv2
import numpy as np
from fastapi import FastAPI, APIRouter, Body
from fastapi.responses import StreamingResponse
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket

from app.apis.api_v1.login import router as login_router
from app.apis.api_v1.user import router as user_router
from app.apis.api_v1.disease import router as disease_router
from app.apis.api_v1.pest import router as pest_router
from app.apis.api_v1.plant import router as plant_router
from app.chat.spark_chat import chat
from app.core.config import PREDICT_PATH
from app.middleware.cors_midd import setup_cors
from app.vision.yolo_predict import yolo, frame_predict

API_VERSION = "/api/v1"

app = FastAPI()
setup_cors(app)

v1 = APIRouter(prefix=API_VERSION)

v1.include_router(login_router, tags=["login"])
v1.include_router(user_router, tags=["user"])
v1.include_router(disease_router, tags=["disease"])
v1.include_router(pest_router, tags=["pest"])
v1.include_router(plant_router, tags=["plant"])

app.include_router(v1)


@app.post("/api/v1/ai-chat")
async def ai_chat(question: str = Body(..., embed=True)):
    async def ext_gen(question_):
        async for g in chat(question_):
            yield g.content

    return StreamingResponse(ext_gen(question), media_type="text/event-stream")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        frame_bytes = await websocket.receive_bytes()

        # 从 bytes 数据中读取图像
        nparr = np.frombuffer(frame_bytes, np.uint8)

        # 解码成图像数组
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        await frame_predict(websocket, image)


# 挂载静态文件目录到 /predict 路由
app.mount("/predict", StaticFiles(directory=PREDICT_PATH), name="predict")
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0')
