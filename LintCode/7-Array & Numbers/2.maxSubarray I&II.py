# -*- coding: UTF-8 -*-

"""
Given an array of integers, find a contiguous subarray which has the largest sum.

Have you met this question in a real interview? Yes
Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    # O(n) space
    def maxSubArray(self, nums):
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(max(nums[i]+sums[i-1], nums[i]))
            print sums
        return max(sums)

    # O(1) space
    def maxSubArray2(self, nums):
        a = nums
        cur_max = a[0]
        max_here= a[0]
        for i in range(1, len(a)):
            max_here = max(max_here+a[i], a[i])
            if max_here > cur_max:
                cur_max = max_here
            print cur_max, max_here
        return cur_max


#so = Solution()
#a = [-2,2,-3,4,-1,2,1,-5,3]
#so.maxSubArray2(a)

#"""
#Given an array of integers, find two non-overlapping subarrays which have the largest sum.
#
#The number in each subarray should be contiguous.
#
#Return the largest sum.
#Example
#For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.
#
#Note
#The subarray should contain at least one number
#
#Challenge
#Can you do it in time complexity O(n) ?
#"""
    # O(n^2) time, will have TLE
    def maxTwoSubArrays(self, nums):
        n = len(nums)
        left = []
        right = []
        for i in range(1, n):
            left.append(self.maxsub(nums[:i]))
            right.append(self.maxsub(nums[i:]))
        re = left[0] + right[0]
        for i in range(len(left)):
            re = max(left[i] + right[i], re)
        print left
        print right
        return re

    def maxsub(self, a):
        cur_max = a[0]
        max_here= a[0]
        for i in range(1, len(a)):
            max_here = max(max_here+a[i], a[i])
            if max_here > cur_max:
                cur_max = max_here
        return cur_max

    # O(n) method
    def maxTwoSubArrays2(self, nums):
        n = len(nums)
        a = [nums[0]]
        # am, bm are global max
        am = [nums[0]]
        for i in range(1, n):
            a.append(max(a[i-1] + nums[i], nums[i]))
            am.append(max(am[i-1], a[i]))
        b = list(nums)
        bm = list(nums)
        for j in range(n-2, -1, -1):
            b[j] = max(b[j+1] + nums[j], nums[j])
            bm[j] = max(bm[j+1], b[j])
        mx = -65535
        for i in range(n-1):
            mx = max(mx, am[i] + bm[i+1])

        return mx


so = Solution()
#print so.maxTwoSubArrays2([1,3,-1,2,-1,2])
so.maxTwoSubArrays2([-1,-2,-3,-100,-1,-50])

