"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
"""
from LeetcodeDefaultDataStructure import *

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            self.s = []
            return
        s = [root]
        while root.left:
            s.append(root.left)
            root = root.left
        self.s = s


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.s:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        node = self.s.pop()
        if node.right:
            right_node = node.right
            self.s.append(right_node)
            while right_node.left:
                self.s.append(right_node.left)
                right_node = right_node.left
        return node.val

node = TreeNode(2)
node.left = TreeNode(1)
node.right = TreeNode(3)
so = BSTIterator(node)
print so.s[0].val
print so.hasNext()
print so.next()
while so.hasNext():
    print so.next()
