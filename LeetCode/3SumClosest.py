"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        diff = nums[0]+ nums[1]+ nums[2] - target
        nums.sort()
        # Be careful for the bound here, must make sure the subarray has at least 2 elements
        for i in xrange(len(nums)-2):
            tft = target - nums[i]
            temp = self.twoSum(nums[i+1:], tft)
            if abs(temp) < abs(diff):
                diff = temp
        return diff + target

    def twoSum(self, a, target):
        l = 0
        r = len(a) -1
        mindiff = a[l] + a[l + 1] - target
        while r > l:
            if a[l] + a[r] == target:
                return 0
            if abs(a[l]+a[r]-target) < abs(mindiff):
                mindiff = a[l]+a[r]-target
            if a[l] + a[r] > target:
                r -= 1
            else:
                l += 1
        return mindiff

so = Solution()
print so.threeSumClosest([1,-1,1], 0)
