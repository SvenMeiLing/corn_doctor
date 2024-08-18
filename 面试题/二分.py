# -*- coding: utf-8 -*-
# FileName: 二分.py
# Time : 2024/8/10 13:01
# Author: zzy
def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


lst = [-1, 0, 3, 5, 9, 12]
print(search(lst, 5))
