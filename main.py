# -*- coding: utf-8 -*-
# FileName: main.py
# Time : 2024/6/13 20:01
# Author: zzy
import asyncio
import base64
import logging
from contextlib import asynccontextmanager
from io import BytesIO

import coloredlogs
from PIL import Image
from aioredis import ConnectionPool, Redis
from fastapi import FastAPI, APIRouter, Body
from fastapi.responses import StreamingResponse
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket
from ultralytics import YOLO

from app.apis.api_v1.disease import router as disease_router
from app.apis.api_v1.login import router as login_router
from app.apis.api_v1.pest import router as pest_router
from app.apis.api_v1.plant import router as plant_router
from app.apis.api_v1.user import router as user_router
from app.utils.spark_chat import chat
from app.core.config import PREDICT_PATH, MODEL_PATH, REDIS_HOST, REDIS_PORT
from app.middleware.cors_midd import setup_cors
from app.vision.yolo_predict import frame_predict

API_VERSION = "/api/v1"

# 配置日志
logger = logging.getLogger("uvicorn")
coloredlogs.install(level='INFO', logger=logger)
model = None


async def startup_preload_model():
    logger.info("正在预加载模型")
    global model
    model = YOLO(MODEL_PATH)
    model.predict(None)
    logger.info("模型预加载完成")


async def startup_connection_redis():
    logger.info("正在连接redis")
    # 建立redis连接池
    pool = ConnectionPool(
        max_connections=70000
    )
    # 挂载到全局
    app.state.redis = Redis(  # type:ignore
        host=REDIS_HOST,
        port=REDIS_PORT,
        connection_pool=pool,
    )


async def start_celery_task():
    """
    自动开启定时任务(实现默认对redis的数据增长)
    """
    worker_cmd = ['celery', '-A', 'app.tasks.auto_add_toredis', 'worker', '--loglevel=info', '-P', 'eventlet']
    beat_cmd = ['celery', '-A', 'app.tasks.auto_add_toredis', 'beat', '--loglevel=info']

    # 启动 Worker 进程
    worker_process = await asyncio.create_subprocess_exec(*worker_cmd, stdout=asyncio.subprocess.PIPE,
                                                          stderr=asyncio.subprocess.PIPE)
    logger.info(f'Celery Worker started with PID {worker_process.pid}')

    # 启动 Beat 进程
    beat_process = await asyncio.create_subprocess_exec(*beat_cmd, stdout=asyncio.subprocess.PIPE,
                                                        stderr=asyncio.subprocess.PIPE)
    logger.info(f'Celery Beat started with PID {beat_process.pid}')


@asynccontextmanager
async def lifespan(fast_app: FastAPI):
    # 生命周期操作
    await asyncio.gather(
        startup_connection_redis(), startup_preload_model(),  # start_celery_task()
    )
    logger.info("All operations have been completed")
    yield
    # 此处后置操作关闭redis连接
    fast_app.state.redis.close()  # type: ignore


app = FastAPI(lifespan=lifespan)
# 设置中间件
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
    """
    用于响应文本流
    :param question: 用户问题
    """

    async def ext_gen(question_):
        async for g in chat(question_):
            yield g.content

    return StreamingResponse(ext_gen(question), media_type="text/event-stream")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    接收多帧图像识别, 并send数据
    """
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        image_data = base64.b64decode(data.split(",")[1])
        image = Image.open(BytesIO(image_data))

        # 预测每帧图像并响应
        await frame_predict(websocket, image, model)


# 挂载静态文件目录到 /predict 路由
app.mount("/predict", StaticFiles(directory=PREDICT_PATH), name="predict")
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0')
