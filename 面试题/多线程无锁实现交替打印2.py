# -*- coding: utf-8 -*-
# FileName: 多线程无锁实现交替打印.py
# Time : 2024/8/9 16:39
# Author: zzy
from threading import Thread, Event

event_1 = [True]
event_2 = [False]


def func_a(ev1, ev2):
    for i in range(11):
        if ev1[0]:
            print("a")
            ev1[0] = False
            ev2[0] = True


def func_b(ev1, ev2):
    for i in range(11):
        if ev2[0]:
            print("b")
            ev2[0] = False
            ev1[0] = True


t1 = Thread(target=func_a, args=(event_1, event_2))
t2 = Thread(target=func_b, args=(event_1, event_2))

t1.start()
t2.start()
