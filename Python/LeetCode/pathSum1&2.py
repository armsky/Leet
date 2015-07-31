"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from LeetcodeDefaultDataStructure import *

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def pathSum(self, root, sum):
        result = []
        if root:
            stack = [root.val]
            self.dfs(root, sum-root.val, stack, result)
        return result

    def dfs(self, root, sum, stack, result):
        if sum == 0 and not root.left and not root.right:
            result.append(stack)
        # Must use stack + [] to create new list (not stack.append())
        if root.left:
            self.dfs(root.left, sum-root.left.val, stack + [root.left.val], result)
        if root.right:
            self.dfs(root.right, sum-root.right.val, stack + [root.right.val], result)

so = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)

print so.pathSum(a, 6)
