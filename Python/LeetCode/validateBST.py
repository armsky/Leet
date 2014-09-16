"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if (root.left == None or root.left.val < root.val) and (root.right == None or root.right.val > root.val):
            if self.isValidBST(root.left) and self.isValidBST(root.right):
                return True
            return False
        return False

root = TreeNode(10)
node1 = TreeNode(5)
root.left = node1
node2 = TreeNode(15)
root.right = node2
node2.left = TreeNode(6)
node2.right = TreeNode(20)

solu = Solution()

print solu.isValidBST(root)

