# -*- coding: utf-8 -*-
# FileName: fib.py
# Time : 2024/8/9 22:32
# Author: zzy
def fib(n):  # 6
    """1+1+2+3+5+8+13"""
    # f[n]=f[n-1]+f[n-2]
    if n == 1:
        return n
    if n == 2:
        return n
    return fib(n - 1) + fib(n - 2)

"""
5+4
3+2
1+0
"""
print(fib(6))
