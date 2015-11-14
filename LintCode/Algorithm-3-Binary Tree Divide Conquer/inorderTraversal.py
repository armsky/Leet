"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,3,2].
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        re = []
        if not root:
            return re
        self.inorder(root, re)
        return re

    def inorder(self, root, re):
        if not root:
            return
        self.inorder(root.left, re)
        re.append(root.val)
        self.inorder(root.right, re)

    def inorderTraversal2(self, root):
        if not root:
            return []
        re = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                re.append(root.val)
                root = root.right
        return re

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
