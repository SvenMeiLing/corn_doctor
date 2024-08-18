# -*- coding: utf-8 -*-
# FileName: 装饰器类.py
# Time : 2024/8/10 1:32
# Author: zzy
import time
from typing import Callable


class Timer:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print(time.time(), "s")
            ret = func(*args, **kwargs)
            print(time.time(), 'e')
            return ret

        return wrapper


def add(a, b):
    return a + b


add = Timer(prefix="current time:")(add)

print(add(1, 2))
