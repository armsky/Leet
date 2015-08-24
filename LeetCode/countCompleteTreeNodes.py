"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

class Solution:
    # @param {TreeNode} root
    # @return {integer}

    # Naive solution, will have TLE
    def countNodes(self, root):
        if not root:
            return 0
        import Queue
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(root)
        count = 1
        while not q1.empty():
            node = q1.get()
            if node:
                count += 1
            else:
                return count
            q2.put(node.left)
            q2.put(node.right)
            if q1.empty():
                q1, q2 = q2, q1

    # Use binary search to find how many nodes in last level.
    # Node number n = 2^h in last level, binary search takes O(log2 n) = O(h), each search also takes
    # O(h) from root to leaf, so total time complexity is O(h^2)
    def countNodes(self, root):
        if not root:
            return 0
        h = 0
        node = root
        while node.left:
            node = node.left
            h += 1
        l = 0
        r = 2 ** h - 1
        while l <= r:
            m = (l+r)/2
            if self.hasNode(root, m, h):
                l = m + 1
            else:
                r = m - 1
        return 2 ** h + r

    def hasNode(self, root, m, h):
        node = root
        for i in xrange(h-1, -1, -1):
            if m & 1 << i:
                node = node.right
            else:
                node = node.left
        return node is not None

    # Recursive solution
    # O(h^2)
    def countNodes(self, root):
        if not root:
            return 0
        l = 0
        r = 0
        lnode = root
        rnode = root
        while lnode.left:
            l += 1
            lnode = lnode.left
        while rnode.right:
            r += 1
            rnode = rnode.right
        if l == r:
            return (2 << l) -1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) +1
