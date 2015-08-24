"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.


Anwser: paths[i][j] = paths[i-1][j] + paths[i][j-1]
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        grid = [[0]*n for i in range(m)]
        grid[m-1][n-1] = 0
        for i in range(m-1,0-1,-1):
            for j in range(n-1,0-1,-1):
                if i==m-1 or j==n-1:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i+1][j]+grid[i][j+1]
        return grid[0][0]

solution = Solution()
print solution.uniquePaths(7,3)
print solution.uniquePaths(1,2)

