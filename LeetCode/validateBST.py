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
        #Python basically has no limit for int
        return self.isValidSubTree(root, float("-infinity"), float("infinity"))
    def isValidSubTree(self, node, minVal, maxVal):
        if node == None:
            return True
        #important
        if node.val <= minVal or node.val >= maxVal:
            return False
        return self.isValidSubTree(node.left, minVal, node.val) and self.isValidSubTree(node.right, node.val, maxVal)

root = TreeNode(10)
node1 = TreeNode(5)
root.left = node1
node2 = TreeNode(15)
root.right = node2
node2.left = TreeNode(6)
node2.right = TreeNode(20)

solu = Solution()

print solu.isValidBST(root)

