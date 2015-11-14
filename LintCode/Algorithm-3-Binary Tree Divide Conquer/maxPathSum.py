"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Have you met this question in a real interview? Yes
Example
Given the below binary tree:

  1
 / \
2   3
return 6.
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    import sys

    def maxPathSum(self, root):
        # sinlgeSum could contain 0..n nodes
        # maxSum must have at least 1 node
        maxSum, singleSum = self.helper(root)
        return maxSum

    def helper(self, root):
        if not root:
            # maxSum is globally max in tree, it must exist and must >= min_int
            return -sys.maxint-1, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        # singleSum must >= 0, because tree node may have value < 0
        singleSum = max(left[1] + root.val, right[1] + root.val, 0)
        maxSum = max(left[0], right[0], left[1] + right[1] + root.val)
        return maxSum, singleSum

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
