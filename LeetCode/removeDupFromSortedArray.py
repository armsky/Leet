"""
Given a sorted array, remove the duplicates in place such that each element appear
only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i, j = 0, 1
        for j in range(1, len(A)):
            if A[j] == A[i]:
                A[j] = " "
                j = j + 1
            else:
                i += 1
                A[i] = A[j]
                #A[j] = " "
                j += 1
            print A
        A = A[:i+1]
        print A
        return i+1
    def removeDuplicates2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        i = 1
        for j in xrange(1, n):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i

so = Solution()
A = [1,1,2,2,3,4,5,5,5,6,7,8,8,9,9]
B = [1,2]
print so.removeDuplicates2(A)
print so.removeDuplicates2(B)
