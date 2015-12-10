"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # This only works when there is no loop
        if not head:
            return None
        table = {}
        b = RandomListNode(head.label)
        a = head
        heada = a
        headb = b
        while a.next:
            b.next = RandomListNode(a.next.label)
            a = a.next
            b = b.next
        a = heada
        b = headb
        while a:
            if a.random:
                table[a.random.label] = b
            if b.label in table:
                table[b.label].random = b
            a = a.next
            b = b.next

        return headb

    def copyRandomList2(self, head):
        if not head:
            return None
        table = {}
        dummy = RandomListNode(0)
        b = RandomListNode(0)
        a = head
        pre = dummy
        dummy.next = b
        while a:
            if a in table:
                b = table[a]
            else:
                b = RandomListNode(a.label)
                table[a] = b
            pre.next = b
            if a.random:
                if a.random in table:
                    b.random = table[a.random]
                else:
                    b.random = RandomListNode(a.random.label)
                    table[a.random] = b.random
            pre = pre.next
            a = a.next
        return dummy.next

