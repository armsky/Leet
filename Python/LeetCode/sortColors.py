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
        i = 0
        size = len(nums)
        for x in xrange(2): # Only need to sort '0' and '1', '2's will be already sorted
            j = size -1
            while i < j:
                while nums[i] == x:
                    if i >= size-1:
                        break
                    i += 1
                while nums[j] != x:
                    if j <= 0:
                        break
                    j -= 1
                if i < j and i < size and j > -1:
                    nums[i], nums[j] = nums[j], nums[i]
        print nums

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
