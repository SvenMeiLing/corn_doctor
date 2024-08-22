# -*- coding: utf-8 -*-
# FileName: 最长回文子序列.py
# Time : 2024/8/21 21:38
# Author: zzy

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # 设置起始位置
        start = max(0, i - len(res) - 1)
        # 假设的回文子串
        temp = s[start: i + 1]
        # 如果满足该字串满足回文子串（逆序与正序相等）
        if temp == temp[::-1]:
            # 将结果设为这个假设的临时字串
            res = temp
        else:
            # 如果假设为错， 则原地略过第一个值
            temp = temp[1:]
            # 如果该值是回文子串
            if temp == temp[::-1]:
                # 设置结果
                res = temp
    return res


print(longestPalindrome("eabcb"))
