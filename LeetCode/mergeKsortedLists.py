"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(a, b):
    dummy = ListNode(0)
    if a is not None:
        dummy.next = a
    else:
        dummy.next = b
    cur = dummy
    while a is not None and b is not None:
        if a.val < b.val:
            a = a.next
        else:
            next = b.next
            cur.next = b
            b.next = a
            b = next
        cur = cur.next
    if a is not None:
        cur.next = a
    if b is not None:
        cur.next = b
    return dummy.next

def helper(lists, l, r):
    while r > l:
        m = (l+r)/2
        return merge(helper(lists, l, m), helper(lists, m+1, r))
    return lists[l]

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return None
        return helper(lists, 0, k-1)

first = ListNode(1)
second = ListNode(10)
third = ListNode(101)
first.next = second
second.next = third
A = []
A.append(first)
A.append(ListNode(5))
A.append(ListNode(3))


so = Solution()
print so.mergeKLists(A).next.next.next.next.val
