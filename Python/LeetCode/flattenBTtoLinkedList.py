"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree, each node's right child
points to the next node of a pre-order traversal.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

    #solution 1: use recursive
    def flatten(self, root):
        if root == None:
            return None
        self.convertToList(root)

    def convertToList(self, root):
        if root == None:
            return
        #must convert right tree first, use a temp to store the right tree
        tempRight = self.convertToList(root.right)
        root.right = self.convertToList(root.left)
        root.left = None
        while root.right != None:
            root = root.right
        root.right = tempRight
        return root

