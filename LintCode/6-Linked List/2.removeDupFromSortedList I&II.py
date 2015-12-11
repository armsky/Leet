"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if not head:
            return head
        nex = head.next
        cur = head
        while cur:
            while nex and nex.val == cur.val:
                nex = nex.next
            cur.next = nex
            cur = cur.next
        return head
"""
Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next
