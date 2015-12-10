# -*- coding: UTF-8 -*-

"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Have you met this question in a real interview? Yes
Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Note
You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        i = 0
        n = len(nums) -1
        j = n
        while i < j:
            while nums[i] < k:
                i += 1
                if i > n:
                    return i
            while nums[j] >= k:
                j -= 1
                if j <= 0:
                    return i
            # This if statement is important
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return i

a = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
so = Solution()

so.partitionArray(a, 9)
print a

