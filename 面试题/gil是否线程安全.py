# -*- coding: utf-8 -*-
# FileName: gil是否线程安全.py
# Time : 2024/8/5 9:27
# Author: zzy
import threading

counter = 0


def f():
    global counter
    counter_next = counter
    for _ in range(1000000):
        counter = counter_next
        counter_next = counter + 1


t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
