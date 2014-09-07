"""
Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

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
    # @return a list node

    #still use fast/slow runner, but be noted.
    #the node they meet is NOT the node that cycle starts!
    #see: http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html
    #fast runs: 2t = X + mY + K
    #slow runs:  t = X + nY + K
    # => X + K = (m-2n)Y
    # Means next X steps, slow will go to the start of the circle
    def detectCycle(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                #set slow to head, let slow and fast both run X steps
                #whey will meet at the cycle start
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

head = ListNode(3)
in1 = ListNode(2)
in2 = ListNode(0)
in3 = ListNode(-4)
head.next = in1
in1.next = in2
in2.next = in3
in3.next = in1

solution = Solution()
print solution.detectCycle(head)
