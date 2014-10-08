"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        elif head.next == None or k == 0:
            return head
        num = 1
        node = head
        while node.next != None:
            num += 1
            node = node.next
        k = k % num
        if k == 0:
            return head
        node = head
        end = head
        for i in range(k):
            if node.next != None:
                node = node.next
            else:
                return head
        while node.next != None:
            node = node.next
            end = end.next
        newHead = end.next
        node.next = head
        end.next = None
        return newHead

so = Solution()
a = ListNode(1)
a.next = ListNode(2)
print so.rotateRight(a, 1)
