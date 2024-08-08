# -*- coding: utf-8 -*-
# FileName: python自带的缓存.py
# Time : 2024/8/8 11:18
# Author: zzy
def f():
    xy = 'xy'


print(f.__code__.co_varnames[0])
