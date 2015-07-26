# From LeetCode definition
import sys
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


