# -*- coding: utf-8 -*-
# FileName: 生成器的示例.py
# Time : 2024/8/7 20:41
# Author: zzy
import random


def producer(con):
    """生产者"""
    next(con)
    while True:
        con.send(random.randint(1, 10))


def consumer():

    while 1:
        ri = yield
        print(ri)


c = consumer()
producer(c)


