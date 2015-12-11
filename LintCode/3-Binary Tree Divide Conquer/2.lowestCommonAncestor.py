"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Have you met this question in a real interview? Yes
Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7

"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

# NOTE: Binary tree might not a BST.
    def lowestCommonAncestor(self, root, A, B):
        if root in (None, A, B):
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

a = TreeNode(1)
so = Solution()
print so.lowestCommonAncestor(a, 1, 1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c


