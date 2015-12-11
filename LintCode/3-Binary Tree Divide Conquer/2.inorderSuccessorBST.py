"""
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

Example
Given tree = [2,1] and node = 1:

  2
 /
1
return node 2.

Given tree = [2,1,3] and node = 2:

  2
 / \
1   3
return node 3.

Note
If the given node has no in-order successor in the tree, return null.

Challenge
O(h), where h is the height of the BST.
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # If the node has right, return it
        # If not, traversal down to find the successor
        if not root:
            return None
        if p.right:
            succ = p.right
            while succ.left:
                succ = succ.left
            return succ
        succ = None
        while root:
            if p.val > root.val:
                root = root.right
            elif p.val < root.val:
                succ = root
                root = root.left
            else:
                break
        return succ


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
