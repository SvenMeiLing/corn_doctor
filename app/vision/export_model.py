# -*- coding: utf-8 -*-
# FileName: export_model.py
# Time : 2024/8/15 22:11
# Author: zzy

class A:
    def __new__(cls, arg):
        obj = super().__new__(cls)
        obj.arg = arg + 1
        return obj

    def __init__(self, arg):
        self.arg = arg + 1


obj = A(2)
print(obj.arg)
