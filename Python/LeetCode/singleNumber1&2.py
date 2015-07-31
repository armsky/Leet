"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}

    # 1. use hashtable, will use extra memory
    def singleNumber(self, nums):
        table = {}
        for num in nums:
            if num not in table:
                table[num] = "1"
            else:
                table[num] = "2"
        for key, value in table.iteritems():
            if value == "1":
                return key

    # 2. XOR two same numbers will be 0, so the last one will appear only once.
    #   No extra memory will be used.
    def singleNumber(self, nums):
        res = nums[0]
        for i in xrange(1, len(nums)):
            res = res ^ nums[i]
        return res
