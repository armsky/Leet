"""
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

Challenge
O(log n) time.
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A or not target:
            return [-1, -1]
        result = []
        # left bound
        l = 0
        r = len(A) - 1
        while r > l:
            m = (r+l)/2
            if A[m] < target:
                l = m + 1
            else:
                r = m
        if A[l] == target:
            result.append(l)
        else:
            return [-1, -1]
        # right bound
        r = len(A) - 1
        while r - l > 1:
            m = (r+l)/2
            if A[m] > target:
                r = m - 1
            else:
                l = m
        if A[r] == target:
            result.append(r)
        elif A[l] == target:
            result.append(l)
        # right bound must exist
        return result


so = Solution()
print so.searchRange([1,3,5,6,8,9], 9)

"""
Test cases:
    1. ([1,2,3,4,5,6], 6)


NOTE:
    1. Use case 1 to decide left bound
    2. Use case 2 to decide right bound
"""
