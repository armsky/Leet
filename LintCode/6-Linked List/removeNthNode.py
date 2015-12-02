"""
Given a linked list, remove the nth node from the end of list and return its head.

Have you met this question in a real interview? Yes
Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.
Note
The minimum number of nodes in list is n.
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        tail = head
        while n > 0:
            tail = tail.next
            n -= 1

        pre = ListNode(0)
        pre.next = head
        while tail:
            tail = tail.next
            pre = pre.next
        pre.next = pre.next.next
        if head.next == pre.next:
            return pre.next
        return headso = Solution()


