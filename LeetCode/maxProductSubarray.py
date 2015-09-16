"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    # need to track the current max and min, since two negetive products a positive.
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        cur_max, cur_min, ans = nums[0], nums[0], nums[0]

        for i in xrange(1, len(nums)):
            temp = cur_max
            cur_max = max(max(cur_max * nums[i], cur_min * nums[i]), nums[i])
            cur_min = min(min(temp * nums[i], cur_min * nums[i]), nums[i])
            ans = max(ans, cur_max)
        return ans
