"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

# NOTE:
# 1. Sort the list A
# 2. Pick A[i], and find target of -A[i], becomes a problem of 2 Sum
#       Only need to scan A[i+1:] each time
# 3. Be careful about the duplicate value
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            target = 0 - nums[i]
            temp = self.twosum(nums[i+1:], target)
            if temp:
                for one in temp:
                    if one not in result:
                         result.append(one)
        return result

    # This may have more than one pair of result
    def twosum(self, a, target):
        table = {}
        re = []
        for num in a:
            if target - num not in table:
                table[num] = 1
            else:
                re.append([0-target, target-num, num])
        if re:
            return re
        else:
            return None
