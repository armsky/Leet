"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean

    #withoud extra space
    #1. fast runner and slow runner
    def hasCycle(self, head):
        #remember the empty {} !!!
        if head is None:
            return False
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

head = ListNode(3)
in1 = ListNode(2)
in2 = ListNode(0)
in3 = ListNode(-4)
head.next = in1
in1.next = in2
in2.next = in3
in3.next = in1

solution = Solution()
print solution.hasCycle(head)
