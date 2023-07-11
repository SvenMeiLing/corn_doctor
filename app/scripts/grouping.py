# -*- coding: utf-8 -*-
# FileName: grouping.py
# Time : 2023/6/12 10:39
# Author: zzy
import pprint
from itertools import groupby
from typing import Iterable


def grouping(iterable: Iterable, express=lambda tup: tup[0]):
    """
    利用表达式 分组
    :param iterable: 可迭代对象,
    :param express: lambda表达式
    :return: 分组后的数据
    """
    grp = groupby(iterable, express)
    for _, value in grp:
        yield list(value)


def complete_list(res):
    res = list(grouping(res))
    index = 6
    for grp in res:
        if grp[-1][-1] != '6':
            grp.insert(6, [grp[0][0], 0, '6'])
        for index, g in enumerate(grp):
            print(g)
            if g[2] == str(index):
                ...
            else:
                grp.insert(index, [g[0], g[1], str(index)])
    return res


if __name__ == '__main__':
    print(complete_list(lst))
