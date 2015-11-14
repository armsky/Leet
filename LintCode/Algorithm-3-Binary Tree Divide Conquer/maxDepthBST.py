"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Given a binary tree as follow:

  1
 / \
2   3
   / \
  4   5
The maximum depth is 3.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        depth = 0
        return self.next(depth, root)

    def next(self, depth, node):
        if not node:
            return depth
        depth += 1
        return max(self.next(depth, node.left), self.next(depth, node.right))

    def maxDepth2(self, root):
        if not root:
            return 0
        depth = 0
        stack = [root]
        temp = []
        while stack:
            while stack:
                node = stack.pop()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth += 1
            stack = temp
            temp = []
        return depth


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.preorderTraversal2(a)
