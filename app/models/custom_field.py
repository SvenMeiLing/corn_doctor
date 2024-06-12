# -*- coding: utf-8 -*-
# FileName: custom_field.py
# Time : 2024/6/12 15:43
# Author: zzy
import datetime
from dataclasses import dataclass, InitVar
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


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


if __name__ == '__main__':
    class M(BaseModel):
        f: FilePath = Field(
            None, example="home/media/2024/07/19/dsadjaki1u23iedbai.png",
            description="植株图片存储地址(相对路径)"
        )


    m = M(f=FilePath("1.jpg"))
    print(m.dict())
