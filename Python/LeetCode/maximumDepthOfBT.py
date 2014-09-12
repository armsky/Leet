"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        lmax = self.maxDepth(root.left)
        rmax = self.maxDepth(root.right)
        return max(lmax, rmax) +1

head = TreeNode(3)
in1 = TreeNode(2)
in2 = TreeNode(0)
in3 = TreeNode(-4)
head.left = in1
in1.left = in2
head.right = in3
#in3.next = in1

solution = Solution()
print solution.maxDepth(head)
