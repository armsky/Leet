"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        res = [-1,-1]
        if not nums:
            return res
        ll = 0
        lr = len(nums) -1
        while ll <= lr:
            m = (ll + lr) / 2
            if nums[m] < target:
                ll = m+1
            else:
                lr = m-1
        rl = ll
        rr = len(nums) -1
        while rl <= rr:
            m = (rl + rr) / 2
            if nums[m] <= target:
                rl = m+1
            else:
                rr = m-1
        if ll <= rr:
            return [ll, rr]
        return res
