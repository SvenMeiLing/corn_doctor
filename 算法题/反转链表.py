# -*- coding: utf-8 -*-
# FileName: 反转链表.py
# Time : 2024/8/2 12:09
# Author: zzy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

