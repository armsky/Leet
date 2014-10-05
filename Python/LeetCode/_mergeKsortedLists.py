"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
import heapq

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap =[]
        for node in lists:
            if node != None:
                heap.append((node.val,node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            popNode = heapq.heappop(heap)
            curr.next = popNode[1]
            curr = curr.next
            if popNode[1].next:
                heapq.heappush(heap,(popNode[1].next.val,popNode[1].next))
        return head.next

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
