"""
Sort a linked list in O(n log n) time using constant space complexity.

Have you met this question in a real interview? Yes
Example
Given 1-3->2->null, sort it to 1->2->3->null.
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        tail = mid.next
        mid.next = None
        head = self.sortList(head)
        tail = self.sortList(tail)
        return self.merge(head, tail)

    def merge(self, a, b):
        dummy = ListNode(0)
        head = dummy
        while a and b:
            if a.val < b.val:
                head.next = a
                a = a.next
            else:
                head.next = b
                b = b.next
            head = head.next
        if a:
            head.next = a
        if b:
            head.next = b
        return dummy.next


    def find_mid(self, head):
        if not head:
            return None
        a = head
        b = head.next
        while b and b.next:
            a = a.next
            b = b.next.next
        return a

so = Solution()
a = ListNode(1)
a.next = ListNode(-1)
so.sortList(a)
