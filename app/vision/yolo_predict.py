# -*- coding: utf-8 -*-
# FileName: yolo_predict.py
# Time : 2024/6/30 22:51
# Author: zzy
import base64
import io
import time
from os import PathLike
from pathlib import Path

import cv2
from PIL import Image
from starlette.websockets import WebSocket, WebSocketDisconnect, WebSocketState
from ultralytics import YOLO

from app.vision.handler_count import tensor_counter


def yolo_identify(
        save_to: str | Path,
        source: str | PathLike, model: str | PathLike = None
) -> list:
    """
    通过一个模型路径和图片路径返回识别结果
    :param save_to: 文件保存目录
    :param model: 模型名称.路径
    :param source: 图片路径
    :return:
    """
    if model is None:
        from app.core.config import MODEL_PATH
        model = MODEL_PATH
    model = YOLO(model)
    outputs = model.predict(
        source, imgsz=640, conf=0.5,
        show_boxes=True
    )
    if not save_to.parent.exists():
        save_to.parent.mkdir(parents=True)
    # 手动保存至指定目录
    outputs[0].save(save_to)
    return outputs


def yolo(save_to, source: str | PathLike):
    """
    提供一个目录名称, 返回该目录下所以图片的识别结果
    example:
       [{}]

    :param save_to: 将预测后的文件保存在哪里
    :param source:
    :return:
    """
    res = []
    outputs = yolo_identify(save_to, source)
    for each in outputs:
        updated_result = {
            each.names[key]: value
            for key, value in tensor_counter(each.boxes.cls.data).items()
        }
        # updated_result.update({"save_dir": each.path})  # 缺少后缀名
        res.append(updated_result)
    return res


async def frame_predict(websocket: WebSocket, source, model):
    # 进行预测
    outputs = model.predict(
        source,
        imgsz=320, conf=0.5,
        show_boxes=True, stream=True
    )
    # 获取第一个预测结果的图像
    for output in outputs:
        # 获得ndarray格式图像
        result_image = output.plot()
        # 转化成Image对象, 并变换色彩
        im = Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))  # 加上这一句否者颜色失真
        # 创建内存对象
        io_bytes = io.BytesIO()
        # 保存图像到内存中
        im.save(io_bytes, format="JPEG")
        io_bytes.seek(0)
        # 生成base64的图像链接
        res = f"data:image/jpeg;base64,{base64.b64encode(io_bytes.read()).decode('utf-8')}"
        await websocket.send_text(res)
        print("发送了一帧", time.time())


if __name__ == '__main__':
    ...

    # 假设 bboxes 是 YOLO 预测得到的边界框列表，包含类别、置信度和坐标
    # bboxes 的格式可以是 [(class_id, confidence, (x, y, width, height)), ...]
    # 加载模型
