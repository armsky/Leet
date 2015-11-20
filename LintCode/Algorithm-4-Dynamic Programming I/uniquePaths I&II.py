"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = 1 if dp[i][j-1] != 0 else 0
                    elif j == 0:
                        dp[i][j] = 1 if dp[i-1][j] != 0 else 0
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

so = Solution()
grid = [[0,0,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
grid = [[0,0,0],[0,0,1],[0,0,0],[0,0,0]]
print so.uniquePathsWithObstacles(grid)
