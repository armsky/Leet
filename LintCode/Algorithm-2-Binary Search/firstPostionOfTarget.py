"""
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
"""

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums or not target:
            return -1
        l = 0
        r = len(nums) -1
        while l < r:
            m = l + ((r-l) >> 1)
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if target == nums[l]:
            return l
        else:
            return -1
so = Solution()

"""
Test cases:
    1. ([], None) should return -1. any of them is None should return -1
    2. ([], )
    3. ([], )
    4. ([], )

NOTE: Use case 2 of Binary Search
    split array to two parts: [l, m][m+1, r]
    if target > m, use [m+1, r]
    if target <= m, use [l, m]
    stop when l == r

There is no integer overflow for Pytyhon. The only limitation is memory size.
"""
