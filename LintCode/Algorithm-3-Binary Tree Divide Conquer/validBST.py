"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Have you met this question in a real interview? Yes
Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        if not root:
            return True
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
        for i in range(1, len(re)):
            if re[i] <= re[i-1]:
                return False
        return True

    def idValidBST2(self, root):
        import sys
        maxv = sys.maxint
        minv = -sys.maxint -1
        return self.inRange(root, maxv, minv)


    def inRange(self, root, maxv, minv):
        if not root:
            return True
        if root.val <= minv or root.val >= maxv:
            return False
        return self.inRange(root.left, root.val, minv) and self.inRange(root.right, maxv, root.val)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
