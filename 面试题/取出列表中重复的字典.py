# -*- coding: utf-8 -*-
# FileName: 取出列表中重复的字典.py
# Time : 2024/8/7 21:07
# Author: zzy

lst = [{"a": 1}, {"a": 1}]

# a = [str(i) for i in lst]
# print([eval(i) for i in set(a)])
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
