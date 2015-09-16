"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = [nums[0] if nums[0] > 0 else 0]
        all_negetive = True
        for i in xrange(1, len(nums)):
            if nums[i] > 0:
                all_negetive = False
            if nums[i] + sum[i-1] > 0:
                sum.append(nums[i] + sum[i-1])
            else:
                sum.append(0)
        if all_negetive:
            return max(nums)
        return max(sum)
