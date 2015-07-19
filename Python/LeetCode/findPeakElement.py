"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
    Your solution should be in logarithmic complexity.
"""
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        r = len(nums) - 1
        l = 0
        while r > l:
            m = (r+l)/2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l
