"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}

    # Naive recursive solution, will have TLE
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        while root:
            if root == p or root == q:
                return root
            elif self.isDescendant(root.left, p) and self.isDescendant(root.left, q):
                root = root.left
            elif self.isDescendant(root.right, p) and self.isDescendant(root.right, q):
                root = root.right
            else:
                return root
        return None

    def isDescendant(self, root, node):
        if not root:
            return False
        if root == node:
            return True
        else:
            return self.isDescendant(root.left, node) or self.isDescendant(root.right, node)

    # Optimized recursive version
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root

