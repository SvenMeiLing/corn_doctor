# -*- coding: utf-8 -*-
# FileName: 二分查找.py
# Time : 2024/8/10 10:16
# Author: zzy

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


lst = [0, 2, 4, 5, 8]
print(binary_search(lst, 5))
"""
当目标值大于中间值的时候
左指针前进一步
右指针后退一步
"""
