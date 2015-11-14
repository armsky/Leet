"""
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.

Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        while root.left:
            self.parent = root
            self.cur = root.left
        self.list = [self.cur]
        self.list_size = 1
        self.pos = 0

    def new_list(self):
        cur = self.parent
        self.list = [cur]


    #@return: True if there has next node, or false
    def hasNext(self):
        if self.cur.val >= max_val:
            return False
        return True

    #@return: return next node
    def next(self):
        cur_node = self.list[self.pos]
        self.pos += 1
        if self.pos == self.list_size:


        return cur_node


#Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    #do something for node


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

so = Solution()
print so.inorderTraversal2(a)
