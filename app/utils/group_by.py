# -*- coding: utf-8 -*-
# FileName: group_by.py
# Time : 2024/8/19 22:09
# Author: zzy
from typing import Literal


def fun(f):
    """

    :param f:
    :return:
    """


def group_by_date(data: list, mode: Literal["years", "months", "weeks", "days"]) -> dict:
    """
        :param data: 提供一个类似这样的数据 -->:
            data_years = [
            (mode, '玉米条纹病毒', 4), (mode, '玉米灰斑病', 12),
            (mode, '玉米锈病', 4), (mode, '玉米叶斑病', 1),
            (mode, '玉米条纹病毒', 1), (mode, '玉米锈病', 1), (2026, '玉米锈病', 1)
        ]
        :param mode: 分组字段名称, 可以是->年 月 日
        :return:  [
            (mode, '玉米条纹病毒', 4), (mode, '玉米灰斑病', 12),
            (mode, '玉米锈病', 4), (mode, '玉米叶斑病', 1),
            (mode, '玉米条纹病毒', 1), (mode, '玉米锈病', 1), (2026, '玉米锈病', 1)
        ]
        -----------------------------------------------------------------------
        返回一个分组后的数据 -->:
            example = {
            $mode: [2024, 2025, 2026],
            'datas': {'玉米条纹病毒': [4, 0, 1], '玉米灰斑病': [12, 0, 0], '玉米锈病': [4, 0, 1], '玉米叶斑病': [0, 1, 0]}
        }
    """
    result = {
        # 年份去重
        mode: list(set([i[0] for i in data])),
        "datas": {}
    }
    # 遍历每个元组
    for tup in data:
        # 如果病害名称组不存在与datas中则初始化
        if tup[1] not in result["datas"]:
            # 获取当前年份对应总计的索引
            cur_year_index = result[mode].index(tup[0])
            print("--->", cur_year_index)
            result["datas"][tup[1]] = [0] * len(result[mode])  # 先创建一个填充0的数组
            result["datas"][tup[1]][cur_year_index] = tup[2]
        else:
            # 如果存在, 则肯定是第二年份, 总是获取最后的索引赋值
            result["datas"][tup[1]][len(result["datas"][tup[1]]) - 1] = tup[2]
    return result
