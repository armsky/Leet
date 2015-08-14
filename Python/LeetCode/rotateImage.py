"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.

    # Naive solution, create a new matrix
    def rotate(self, matrix):
        n = len(matrix)
        newm = [[0 for x in range(n)] for y in range(n)]
        for i in xrange(n):
            for j in xrange(n):
                newm[j][n-1-i] = matrix[i][j]

        matrix = newm

    # In-place, loop by loop
    # new_j = i
    def rotate(self, matrix):
        n = len(matrix)
        length = n
        for i in xrange(n/2):
            m = length - 1
            for j in xrange(m):
                temp =                  matrix[i][i+j]
                matrix[i][i+j] =        matrix[i+m-j][i]
                matrix[i+m-j][i] =      matrix[i+m][i+m-j]
                matrix[i+m][i+m-j] =    matrix[i+j][i+m]
                matrix[i+j][i+m] =      temp

            length -= 2

    """
    First swap based on diagnal, and then swap based on midline:
    1 2 ->  1 3 ->  3 1
    3 4     2 4     4 2
    """
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-j-1] =  matrix[i][n-j-1], matrix[i][j]


so = Solution()
so.rotate([[1,2,3],[4,5,6],[7,8,9]])
