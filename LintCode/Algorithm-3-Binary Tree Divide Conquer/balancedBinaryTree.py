"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Given binary tree A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    # I. O(n^2) implementation
    def isBalanced(self, root):
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
