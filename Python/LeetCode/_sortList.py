"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# There is not a lot O(n log n) sorting methods: Merge, Quick and Heap. But Quick is not
# guaranteed. And list does not have O(1) access, so it must be MergeSort

# 1. Use recursion. This is actually not constant space, a log n stack space will be used.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        leftend = slow
        slow = slow.next
        leftend.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        head = cur = ListNode(None)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return head.next

# 2. A real constant space solution


