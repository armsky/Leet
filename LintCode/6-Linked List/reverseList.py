"""
Reverse a linked list.

Example
For linked list 1->2->3, the reversed linked list is 3->2->1
"""
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
    def reverseBetween(self, head, m, n):
        if not head.next:
            return head
        run = head
        for i in range(1, m-1):
            run = run.next
        left = run
        start = run.next
        end = start
        for i in range(m, n):
            end = start.next
        right = end.next
        cur = start
        pre = None
        while cur is not end:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        right.next = cur
        start.next = left
        return head

