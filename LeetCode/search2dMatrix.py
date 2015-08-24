"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

NOTE: Should use Binary Search twice, it's much quicker!!!
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix[0] == None:
            return False
        if target in matrix[0]:
            return True
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                if target in matrix[i-1]:
                    return True
        if target in matrix[-1]:
            return True
        return False

    def bs(self, matrix, target):
        if matrix[0] == None or matrix[0][0] > target:
            return False
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = row-1
        while start <= end:
            mid = (start+end)/2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid -1
            else:
                start = mid + 1
        row = end
        start = 0
        end = col-1
        while start<=end:
            mid = (start+end)/2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return False


s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


print s.searchMatrix(matrix, 3)
print s.bs(matrix, 3)
