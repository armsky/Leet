"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            while A[i] != i+1:
                if A[i] <= 0 or A[i] > len(A) or A[i] == A[A[i]-1]:
                    break
                else:
                    temp = A[A[i]-1]
                    A[A[i]-1] = A[i]
                    A[i] = temp
                    print A
        for i in range(len(A)):
            if A[i] != i+1:
                return i+1
        return len(A)+1

solution = Solution()
print solution.firstMissingPositive([1,2,0])
print solution.firstMissingPositive([3,4,0,2])


