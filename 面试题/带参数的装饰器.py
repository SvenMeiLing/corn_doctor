# -*- coding: utf-8 -*-
# FileName: 带参数的装饰器.py
# Time : 2024/8/7 20:22
# Author: zzy
def wrap(n):
    def wrapper(func):
        print(func, n)

        def inner():
            print(n)
            func()
            return func

        return inner

    return wrapper


@wrap(1)
def f():
    print("im is f")


f()
