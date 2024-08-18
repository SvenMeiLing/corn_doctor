# -*- coding: utf-8 -*-
# FileName: 类装饰器.py
# Time : 2024/8/10 1:45
# Author: zzy
def add_str(cls):
    def __str__(self):
        return str(self.name)
    cls.__str__ = __str__
    return cls


@add_str
class Person:
    def __init__(self, name):
        self.name = name


p = Person('csy')
print(p)
