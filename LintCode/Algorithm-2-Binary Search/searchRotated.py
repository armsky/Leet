"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time

"""
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if not A or not target:
            return -1
        l = 0
        r = len(A) - 1
        while r >= l:
            m = (r+l)/2
            if A[m] > A[r]:
                if target == A[m]:
                    return m
                elif A[l] <= target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # A[m] < A[r]
                if target == A[m]:
                    return m
                if A[m] < target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
"""
Test cases:
    1. ([4,5,1,2,3], 2)
    2. ([3,4,5,1,2], 2)
    3. ([5,6,7,1,2,3,4], 6)

NOTE:
    1. Decide the target could in a ralular sorted subarray, or rotated subarray.

"""
