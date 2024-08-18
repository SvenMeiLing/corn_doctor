# -*- coding: utf-8 -*-
# FileName: 多线程无锁实现交替打印.py
# Time : 2024/8/9 16:39
# Author: zzy
from threading import Thread, Event

event_1 = Event()
event_2 = Event()


def func_a(ev1: Event, ev2: Event):
    for i in range(11):
        ev2.wait()  # 等待线程2释放
        ev2.clear()  # 清除这个标记
        print('a')
        ev1.set()  # 唤醒线程1


def func_b(ev1: Event, ev2: Event):
    for i in range(11):
        ev2.set()  # 唤醒线程2
        ev1.wait()  # 等待线程1
        ev1.clear()  # clear the flag
        print('b')


t1 = Thread(target=func_a, args=(event_1, event_2))
t2 = Thread(target=func_b, args=(event_1, event_2))

t1.start()
t2.start()
