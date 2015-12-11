"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use DFS algorithm to do it.
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    # 1. BFS: Two Queues
    def levelOrder(self, root):
        if not root:
            return []

        import Queue
        q1 = Queue.Queue()
        q1.put(root)
        q2 = Queue.Queue()
        re = []
        temp = []
        while not q1.empty():
            node = q1.get()
            temp.append(node.val)
            if node.left is not None: q2.put(node.left)
            if node.right is not None: q2.put(node.right)
            if q1.empty():
                re.append(temp)
                temp = []
                q1, q2 = q2, q1
        return re

    # 2. BFS: One Queue with dummy nodes
    def levelOrder2(self, root):
        if not root:
            return []
        import Queue
        q = Queue.Queue()
        q.put(root)
        q.put(None) # dummy node
        re = []
        temp = []
        while not q.empty():
            node = q.get()
            if node is None:
                if not temp:
                    break
                q.put(None) # put new dummy node each level
                re.append(temp)
                temp = []
            else:

                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                temp.append(node.val)

        return re

    # 3. BFS: One Queue with counter
    def levelOrder3(self, root):
        if not root:
            return []
        import Queue
        q = Queue.Queue()
        q.put(root)
        re = []
        while not q.empty():
            temp = []
            size = q.qsize()
            for i in range(size):
                node = q.get()
                temp.append(node.val)
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            re.append(temp)
        return re

    # 4. DFS:
    # Pro: _trade_time_for_space_
    def levelOrder4(self, root):
        if not root:
            return None
        max_level = 0
        while True:
            temp = []
            self.dfs(root, temp, 0, max_level)
            if not temp:
                break
            re.append(temp)
            max_level += 1

    def dfs(self, root, temp, cur_level, max_level):
        if not root or cur_level > max_level:
            return
        if cur_level == max_level:
            temp.appned(root.val)
        else:
            self.dfs(root.left, temp, cur_level+1, max_level)
            self.dfs(root.right, temp, cur_level+1, max_level)

    # 5. Recursive
    # This will only return a simple list (not a 2D list as above)
    def levelOrder5(self, root):
        if not root:
            return []
        more, re, temp = [], [], []
        self.recursive(root, more, re, temp)
        return re

    def recursive(self, node, more, re, temp):
        #print re, temp, more
        if node:
            temp.append(node.val)
            more += [node.left, node.right]
        if more:
            self.recursive(more[0], more[1:], re, temp)




a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
c.left = d
a.left = b
a.right = c
d.right = TreeNode(3)
d.left = TreeNode(2)

so = Solution()
print so.levelOrder5(a)
