"""
Given a binary tree, return the preorder traversal of its nodes' values.

Have you met this question in a real interview? Yes
Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3]
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if not root:
            return []
        re = []
        stack = [root]
        while stack:
            node = stack.pop()
            re.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return re

    def preorderTraversal2(self, root):
        re = []
        self.traverse(re, root)
        return re

    def traverse(self, re, node):
        if node:
            re.append(node.val)
            self.traverse(re, node.left)
            self.traverse(re, node.right)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.preorderTraversal2(a)
