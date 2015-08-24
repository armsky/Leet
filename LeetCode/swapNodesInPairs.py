"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify
the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        count = 0
        temp = ListNode(0)
        node = head
        while node != None:
            if count%2 == 0:
                temp = node
                node = node.next
                if count == 0:
                    head = node
            else:
                temp.next = node.next
                node.next = temp
                node = temp.next
            count += 1
        return head
