# -*- coding: UTF-8 -*-

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Have you met this question in a real interview? Yes
Example
Given [1, 0, 1, 2], return [0, 1, 1, 2].
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        i = 0 #points to last index of 0
        j = len(nums) - 1 #points to last index of 2
        k = 0
        while k < j+1:
            if nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
                continue
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1 # must + 1
                continue
            k += 1

a = [2,0,0,1,2,0,2]
so = Solution()
so.sortColors(a)
print a

