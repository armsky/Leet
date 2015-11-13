"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 - 2

[1,3,5,6], 2 - 1

[1,3,5,6], 7 - 4

[1,3,5,6], 0 - 0

Challenge
O(log(n)) time
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        if not A or target < A[0]:
            return 0
        l = 0
        r = len(A) - 1
        while l <= r:
            m = l + ((r-l) >> 1)
            if A[m] == target:
                return m
            elif A[m] > target:
                r = m - 1
            else:
                l = m + 1
        if l == len(A):
            return l
        elif A[l] < target:
            return l+1
        else:
            return l
so = Solution()
print so.searchInsert([1,3,5,6,8,9], 7)

"""
Test cases:
    1. ([], 2), should return 0
    2. ([2], 1), should return 0
    3. ([1,10,1001,201,1001,10001,10007], 10008), should return 7, test right bound
    4. ([1,3,5,6,8,9], 7) should return 4


NOTE: Use Binary Search case 1. find the only element equals to target. At last, r will always in the left of right.
        But, do a judgement at last:
        1. the target bigger than biggest element in list, return l (len of A)
        2. target < left, return l+1
        3. right < target < left, return l
"""
