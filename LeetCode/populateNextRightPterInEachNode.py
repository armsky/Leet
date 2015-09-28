"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):

    # This works for all binary tree (not just perfect binary tree)
    # But this is not using constant space
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        so = [root]
        ss = []
        while any(so):
            for i in xrange(len(so)):
                if so[i] is not None:
                    ss.append(so[i].left)
                    ss.append(so[i].right)
                    if i < len(so) -1:
                        so[i].next = so[i+1]
                    else:
                        so[i].next = None
                else:
                    ss.extend([None, None])
            so = ss
            ss = []

    # A real solution meets the requirements.
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        pre = root
        node = None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                else:
                    cur.right.next = None
                cur = cur.next

            pre = pre.left
