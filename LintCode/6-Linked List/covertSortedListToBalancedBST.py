"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Example
               2
1->2->3  =>   / \
             1   3
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    cur = None
    def sortedListToBST(self, head):
        global cur
        if not head:
            return None
        size = self.getLen(head)
        cur = head
        return self.build(size)

    def getLen(self, a):
        n = 0
        while a:
            a = a.next
            n += 1
        return n

    def build(self, size):
        global cur
        if size <= 0:
            return None
        left = self.build(size/2)
        root = TreeNode(cur.val)
        cur = cur.next
        right = self.build(size -1 -size/2)
        root.left = left
        root.right = right
        return root

    # O(n log n) time
    # No need to keep a global variable current_node
    def sortedListToBST2(self, head):
        if not head:
            return head
        size = self.getLen(head)
        return self.construct(head, size)

    def construct(self, head, size):
        if not head or size==0:
            return None
        root = self.getNode(size/2, head)
        root.left = self.construct(head, size/2)
        root.right = self.construct(self.getNode(size/2 + 1, head), size - size/2 -1)
        return root

    def getNode(self, n, head):
        for i in range(n):
            head = head.next
        return head


so = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
print so.sortedListToBST(a).val

