# -*- coding: utf-8 -*-
# FileName: yolo_predict.py
# Time : 2024/6/30 22:51
# Author: zzy
import uuid
from os import PathLike

from typing.io import IO

from typing import Iterable
from ultralytics import YOLO

from app.vision.handler_count import tensor_counter


def yolo_identify(source: str | PathLike, model: str | PathLike = None) -> list:
    """
    通过一个模型路径和图片路径返回识别结果
    :param model: 模型名称.路径
    :param source: 图片路径
    :return:
    """
    if model is None:
        from app.core.config import MODEL_PATH
        model = MODEL_PATH
    model = YOLO(model)
    outputs = model.predict(
        source, save=True, imgsz=640, conf=0.5,
        show_boxes=True
    )
    return outputs


def temporary_recv(files: Iterable[IO]):
    """
    接受一个存储文件对象的列表
    :param: files 一个可迭代对象, 存放类似IO-object
    :return: PathLike 目录名称
    """
    save_to = "" / uuid.uuid4().hex
    save_to.mkdir(exist_ok=True)
    for file in files:
        with open(save_to / file.name, "wb") as f:  # 保存用户上传的图片
            f.write(file.read())
    return save_to


def yolo(source: str | PathLike):
    """
    提供一个目录名称, 返回该目录下所以图片的识别结果
    example:
       [{}]

    :param source:
    :return:
    """
    res = []
    outputs = yolo_identify(source)
    for each in outputs:
        updated_result = {
            each.names[key]: value
            for key, value in tensor_counter(each.boxes.cls.data).items()
        }
        updated_result.update({"save_dir": each.path})  # 缺少后缀名
        res.append(updated_result)
    return res


if __name__ == '__main__':
    print(yolo_identify(
        r"F:\玉米病害数据库\Maize-diseases.v1i.yolov8\train\6-gls-灰斑病\0a01cc10-3892-4311-9c48-0ac6ab3c7c43___RS_GLSp-9352_90deg_JPG_jpg.rf.6c65375b06c240a27ff7e40e56e8929f.jpg"))
