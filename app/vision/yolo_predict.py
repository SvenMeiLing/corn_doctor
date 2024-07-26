# -*- coding: utf-8 -*-
# FileName: yolo_predict.py
# Time : 2024/6/30 22:51
# Author: zzy
import base64
import io
import time
from os import PathLike
from pathlib import Path

import numpy as np
from PIL import Image
from ultralytics import YOLO

from app.core.config import APP_PATH, PREDICT_PATH
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


if __name__ == '__main__':
    import cv2


    # 假设 bboxes 是 YOLO 预测得到的边界框列表，包含类别、置信度和坐标
    # bboxes 的格式可以是 [(class_id, confidence, (x, y, width, height)), ...]
    # 加载模型
    def func():

        model = YOLO("b2000_c15.pt")

        # 进行预测
        outputs = model.predict(
            r"F:\玉米病害数据库\Maize-diseases.v1i.yolov8\train\6-gls-灰斑病\0a01cc10-3892-4311-9c48-0ac6ab3c7c43___RS_GLSp-9352_90deg_JPG_jpg.rf.6c65375b06c240a27ff7e40e56e8929f.jpg",
            imgsz=640, conf=0.5,
            show_boxes=True
        )
        # 获取第一个预测结果的图像
        result_image = outputs[0].plot()
        im = Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))  # 加上这一句否者颜色失真
        io_bytes = io.BytesIO()
        im.save(io_bytes, format="JPEG")
        io_bytes.seek(0)
        return f"data:image/jpeg;base64,{base64.b64encode(io_bytes.read()).decode('utf-8')}"


    s = time.time()
    for _ in range(10):
        func()
    print(time.time() - s)
