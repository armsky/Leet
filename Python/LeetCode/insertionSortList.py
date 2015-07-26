"""
Sort a linked list using insertion sort.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetcodeDefaultDataStructure import *

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        # Must maintain three pointers, pre, cur and nex
        # pre points to the sorted list's fake head
        # cur points to the node to be inserted
        # nex points to the next node to be inserted
        newhead = ListNode(0)
        cur = head
        # To avoid Time Limit Exceeded, make this optimization
        sortedEnd = head
        while cur:
            nex = cur.next

            if sortedEnd.val < cur.val:
                sortedEnd.next = cur
                cur.next = None
                sortedEnd = cur
            else:
                pre = newhead
                while pre.next and pre.next.val <= cur.val:
                    pre = pre.next
                # This will break the list into two parts
                cur.next = pre.next
                pre.next = cur
            cur = nex
        return newhead.next


so = Solution()
a = ListNode.fromlist()
so.insertionSortList(a)
a.print_list()
