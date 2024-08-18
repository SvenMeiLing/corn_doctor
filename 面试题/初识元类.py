# -*- coding: utf-8 -*-
# FileName: 初识元类.py
# Time : 2024/8/9 20:43
# Author: zzy

class Single:
    _instance = None

    def __init__(self):
        print("init")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MyType(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        create_obj = self.__new__(self)
        self.__init__(create_obj, *args, **kwargs)
        return create_obj


class DIY(metaclass=MyType):
    def __init__(self, name):
        self.name = name


d = DIY("zzy")


class Tet:
    def __init__(self):
        print("init")



Tet()
