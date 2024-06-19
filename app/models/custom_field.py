# -*- coding: utf-8 -*-
# FileName: custom_field.py
# Time : 2024/6/12 15:43
# Author: zzy
import datetime
from dataclasses import dataclass, InitVar
from pathlib import Path
from typing import Optional, Annotated

from pydantic import BaseModel, Field, AfterValidator, WithJsonSchema, PlainSerializer


@dataclass
class FilePath:
    # todo: 输入home/media/2023/12/5/e322c5c4dd094bcde15d5dee44975a5a.jpg的地址后, 帮我校验前缀是否是home/media
    file_path: Path | str  # 文件名称
    base_path: InitVar[Optional[str]] = "/home/media"

    def __post_init__(self, base_path):
        """
        自定义路径前缀, 以适应不同机器之间的差异
        :param base_path: 文件路径前缀
        :return: None
        """
        today = datetime.date.today()
        self.file_path = Path(str(today.year), str(today.month), str(today.day), self.file_path).as_posix().lstrip("/")
        if base_path is not None:
            self.file_path = Path(base_path, self.file_path)

    def __len__(self):
        return len(self.file_path.name)


def after(value: str | FilePath):
    """
    执行逻辑：
    当值传入后立即执行
    所以在使用 value.属性 或者 序列化 dict(),...方法时，都是获取到的处理后的数据
    """
    if isinstance(value, str):
        fp = FilePath(value)
        return fp
    return str(value.file_path)


def plain(value: FilePath) -> str:
    """
    执行逻辑：
    只有在使用 model_dump 等序列化方式时，才会执行，使用 .属性 时并不会执行
    所以如果有数据需要在使用 .属性 或者 序列化时 处理的结果一样，那么请在 after 方法中处理
    如果 after 方法与 plain 方法处理的是一样的，那么可以在这里直接返回值，或者使用 lambda x: x 匿名函数直接返回
    """
    return str(value.file_path)


#  自定义的类型
FilePathStr = Annotated[
    str | FilePath,
    AfterValidator(after),
    PlainSerializer(plain, return_type=str),
    WithJsonSchema({'type': 'string'}, mode='serialization')
]
if __name__ == '__main__':
    class M(BaseModel):
        f: FilePath = Field(
            None, example="home/media/2024/07/19/dsadjaki1u23iedbai.png",
            description="植株图片存储地址(相对路径)"
        )


    m = M(f=FilePath("1.jpg"))
    print(m.dict())
