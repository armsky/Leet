"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.

    # One pass solution
    def sortColors(self, nums):
        redst = 0
        bluest = len(nums) - 1
        i = 0
        while i < bluest + 1:
            if nums[i] == 0:
                nums[i], nums[redst] = nums[redst], nums[i]
                i += 1
                redst += 1
                continue
            if nums[i] == 2:
                nums[i], nums[bluest] = nums[bluest], nums[i]
                # Do not increase i here
                bluest -= 1
                continue
            i += 1
        return

    # counting sort solution
    def sortColors2(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        start = 0
        for i in xrange(3):
            nums[start:count[i]+start] = [i] * count[i]
            start += count[i]
            print nums
        print nums



so = Solution()
so.sortColors2([0,1,0,0,2,0,1,2])
