"""
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        a = head
        b = head.next
        while a and b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False

"""
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Have you met this question in a real interview? Yes
Example
Given -21->10->4->5, tail connects to node index 1，return 10

Challenge
Follow up:

Can you solve it without using extra space?
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # If use extra space
        if not head:
            return None
        table = {}
        while head:
            if head not in table:
                table[head] = True
            else:
                return head
            head = head.next
        return None

    def detectCycle(self, head):
        # If not use extra space
        if not head or not head.next:
            return None
        a = head
        b = head.next
        while a != b:
            if not b or not b.next:
                return None
            a = a.next
            b = b.next.next
        while head != a.next:
            head = head.next
            a = a.next
        return head


