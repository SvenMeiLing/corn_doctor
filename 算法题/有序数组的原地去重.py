# -*- coding: utf-8 -*-
# FileName: 有序数组的原地去重.py
# Time : 2024/7/31 9:24
# Author: zzy
def func(nums):
    fast = 1  # 定义快指针
    slow = fast - 1  # 定义慢指针
    while fast < len(nums):  # fast如果大于等于,则循环中止
        if nums[slow] == nums[fast]:  # 如果两指针结果相同
            nums.remove(nums[slow])  # 移除重复元素
        else:   # 如果两指针所指值不相同, 则向前找+1
            fast += 1
            slow = fast - 1
    return len(nums)


if __name__ == '__main__':
    nums_ = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(func(nums_))
