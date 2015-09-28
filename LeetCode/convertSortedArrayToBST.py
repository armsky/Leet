"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""
from LeetcodeDefaultDataStructure import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums)
        root = TreeNode(nums[n/2])
        root.left = self.sortedArrayToBST(nums[0:n/2])
        print root.left, nums[0:n/2]
        root.right = self.sortedArrayToBST(nums[n/2+1:])
        print root.right, nums[n/2+1:]

        return root

so = Solution()
node = so.sortedArrayToBST([1,3])
#print node.right.val
