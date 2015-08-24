# From LeetCode definition
import sys
import Queue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def fromlist(cls, l):
        head = cls(l[0])
        cur = head
        for i in xrange(1, len(l)):
            head.next = cls(l[i])
            head = head.next
        return cur

    def print_list(self):
        while self:
            sys.stdout.write(str(self.val))
            sys.stdout.write(' ')
            self = self.next
        print


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def fromlist(cls, l):
        if not l:
            return None
        q = Queue.Queue()
        for i in xrange(len(l)):
            node = cls(l[i])
            q.put(node)
