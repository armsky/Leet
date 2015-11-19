"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        dummy = c = ListNode(0)
        carry = 0
        while a or b or carry:
            if a:
                carry += a.val
                a = a.next
            if b:
                carry += b.val
                b = b.next
            carry, val = divmod(carry, 10)
            c.next = ListNode(val)
            c = c.next
        return dummy.next

