# -*- coding: utf-8 -*-
# FileName: custom_type.py
# Time : 2024/6/14 8:30
# Author: zzy


# 官方文档：https://docs.pydantic.dev/dev-v2/usage/types/custom/#adding-validation-and-serialization

import datetime
from typing import Annotated
from pydantic import BaseModel, AfterValidator, PlainSerializer, WithJsonSchema

from app.models.custom_field import FilePath


def after(value: str | FilePath):
    """
    执行逻辑：
    当值传入后立即执行
    所以在使用 .属性 或者 序列化方法时，都是获取到的处理后的数据
    """
    print("after")
    if isinstance(value, str):
        fp = FilePath(value)
        return fp
    return value


def plain(value: FilePath) -> str:
    """
    执行逻辑：
    只有在使用 model_dump 等序列化方式时，才会执行，使用 .属性 时并不会执行
    所以如果有数据需要在使用 .属性 或者 序列化时 处理的结果一样，那么请在 after 方法中处理
    如果 after 方法与 plain 方法处理的是一样的，那么可以在这里直接返回值，或者使用 lambda x: x 匿名函数直接返回
    """
    print("plain 方法执行了", value)
    return str(value.file_path)


# 自定义数据类型
# 实现自定义一个日期时间字符串的数据类型
# 如果我传入的是字符串，那么直接返回，如果我传入的是一个日期类型，那么会转为字符串格式后返回
# 因为在 pydantic 2.0 中是支持 int 或 float 自动转换类型的，所以我这里添加进去，但是在处理时会使这两种类型报错
# 官方文档：https://docs.pydantic.dev/dev-v2/usage/types/datetime/
FilePathStr = Annotated[
    str | FilePath,
    AfterValidator(after),
    PlainSerializer(plain, return_type=str),
    WithJsonSchema({'type': 'string'}, mode='serialization')
]
