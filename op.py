# coding=utf-8
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 2->4->3
        # 5->6->4
        node = tree = ListNode()
        carry = 0
        l1_next = l1.next
        l2_next = l2.next
        while l1_next or l2_next:
            # 6+4=10%10=0
            # carry=1
            # total=0
            c = (l1.val + l2.val) // 10
            total = (l1.val + l2.val) % 10
            if carry:  # 如有进位
                total += c
            tree.next = ListNode(total)
            l1_next = l1_next.next
            l2_next = l2_next.next
            tree = tree.next
        return node


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(l1, l2).next)
print(s.addTwoNumbers(l1, l2).next.next)
