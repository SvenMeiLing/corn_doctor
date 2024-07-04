# -*- coding: utf-8 -*-
# FileName: hasher.py
# Time : 2024/7/1 14:11
# Author: zzy
import datetime
import hashlib
from os import PathLike
from pathlib import Path


def gen_hashed(file_byt: bytes):
    md5 = hashlib.md5(file_byt)
    return md5.hexdigest()


def gen_file_path(filename: str | PathLike) -> str:
    """
    提供文件名称生成这样的路径 -> /$base_dir/2024/07/02/xx.png
    :param filename: 文件名称
    :return:
    """
    today = datetime.date.today()
    file_path = Path(
        str(today.year), str(today.month), str(today.day), filename
    ).as_posix().lstrip("/")
    return file_path


if __name__ == '__main__':
    print(gen_file_path("xx.png"))
