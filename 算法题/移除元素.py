# -*- coding: utf-8 -*-
# FileName: 移除元素.py
# Time : 2024/8/1 19:12
# Author: zzy
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
flag = 0
for i in range(len(nums)):
    if val == nums[flag]:
        nums.remove(nums[flag])
    else:
        flag += 1

print(nums)
