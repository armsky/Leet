# -*- coding: UTF-8 -*-

"""
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        table = {}
        # Put sum as key, if the current sum has been seen before,
        # then there is a zero sum array.
        table[0] = -1 # Must initialize 0 as a key
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in table:
                return [table[sum]+1, i]
            else:
                table[sum] = i

