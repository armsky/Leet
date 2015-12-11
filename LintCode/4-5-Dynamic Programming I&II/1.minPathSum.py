"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                elif i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
        return grid[m-1][n-1]
