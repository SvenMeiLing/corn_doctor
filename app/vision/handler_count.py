# -*- coding: utf-8 -*-
# FileName: handler_count.py
# Time : 2024/6/30 23:31
# Author: zzy
from collections import Counter

from torch import Tensor


def tensor_counter(t: Tensor) -> dict:
    """
    对一个tensor类型数据统计元素个数
    :return: {ele: count, ...}
    """
    return dict(Counter(map(lambda x: int(x), t)).most_common())
