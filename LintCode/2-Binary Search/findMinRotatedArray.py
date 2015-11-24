"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0

Note
You may assume no duplicate exists in the array.
"""

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        if not num:
            return None
        l = 0
        r = len(num) - 1
        while r > l:
            m = (l+r)/2
            if num[m] >= num[r]:
                l = m + 1
            else:
                r = m
        return num[l]
