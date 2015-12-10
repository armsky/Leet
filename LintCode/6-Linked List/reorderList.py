# -*- coding: UTF-8 -*-

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.
For example,
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    # Had TLE because O(n^2)
    def reorderList(self, head):
        if not head or not head.next:
            return
        l = head
        r = head
        while l.next and l.next.next:
            r = l.next
            while r.next:
                rl = r
                r = r.next

            rl.next = None
            r.next = l.next
            l.next = r
            l = r.next

    # Split list in two, reverse the second one, merge them
    def reorderList2(self, head):
        if not head or not head.next:
            return
        a = head
        mid = self.find_mid(head)
        b = self.reverse(mid.next)
        mid.next = None
        self.merge(a, b)


    def merge(self, a, b):
        dummy = ListNode(0)
        i = 0
        while a and b:
            if i%2 == 0:
                dummy.next = a
                a = a.next
            else:
                dummy.next = b
                b = b.next
            i += 1
            dummy = dummy.next
        if a:
            dummy.next = a
        if b:
            dummy.next = b
        while a:
            print a.val

    def find_mid(self, a):
        fast = a.next
        slow = a
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, a):
        pre = None
        cur = a
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

so = Solution()
so.reorderList2(head)
