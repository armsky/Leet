"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

TIPS: Binary search
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        #like cheating... but accepted...
#        for i in A:
#            if i == target:
#                return A.index(i)
#        return -1
        #use binary search
        left = 0
        right = len(A)-1
        while (left <= right):
            mid = (right+left)/2
            if A[mid] == target:
                return mid
            if A[mid] >= A[left]:
                if A[left]<=target and target<A[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
            #A[left] > A[mid]:
                if A[mid] < target and target <= A[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

so = Solution()
print so.search([4,5,6,7,0,1,2], 8)
