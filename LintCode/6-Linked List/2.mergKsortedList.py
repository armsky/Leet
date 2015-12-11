"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # Has TLE
    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = ListNode(0)
        dummy_head = dummy
        h = []
        for head in lists:
            if head:
                h.append(head)
        while h:
            node = self.heappop(h)
            if node.next:
                h.append(node.next)
            dummy.next = node
            dummy = dummy.next
        return dummy_head.next

    def heappop(self, h):
        s = h[0]
        for node in h:
            if node.val < s.val:
                s = node
        h.remove(s)
        return s

    # According to the documentation, use tuples for comparison
    # Heapq will sort by the first element of the tuple
    def mergeKLists2(self, lists):
        if not lists:
            return None
        import heapq
        dummy = ListNode(0)
        dummy_head = dummy
        h = []
        for head in lists:
            if head:
               heapq.heappush(h, (head.val, head))
        while h:
            # remember the second element is the node
            node = heapq.heappop(h)[1]
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))
            dummy.next = node
            dummy = dummy.next
        return dummy_head.next
