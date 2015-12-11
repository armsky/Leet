# -*- coding: UTF-8 -*-

"""
Reverse a linked list.

Example
For linked list 1->2->3, the reversed linked list is 3->2->1
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = head.next
        nex = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            if nex:
                nex = nex.next
        dummy.next.next = None
        return pre

    # More concise version
    def reverse2(self, head):
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
"""
Reverse Linked List II
Reverse a linked list from position m to n.

Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.

Note
Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.
"""

# dummy->1->2->3->4->5->NULL
#        l  s     e  r
    def reverseBetween(self, head, m, n):
        if not head.next or n == m:
            return head
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        for i in range(1, m):
            left = left.next
        start = left.next
        end = start
        for i in range(m, n):
            end = end.next
        right = end.next

        cur = start
        pre = right
        while cur is not right:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        left.next = pre
        return dummy.next

so = Solution()
a = ListNode(1)
b= ListNode(2)
c= ListNode(3)
d= ListNode(4)
e= ListNode(5)
f= ListNode(6)
g= ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
so.reverseBetween(a, 2, 4)

