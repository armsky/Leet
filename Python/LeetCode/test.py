import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node = ListNode(1)
heap = []
heap.append((node.val, node))
heapq.heapify(heap)

