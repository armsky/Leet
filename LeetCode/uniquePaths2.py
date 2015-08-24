"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
#badly implemented, NEED improve

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0]*n for i in range(m)]
        for i in range(m-1,0-1,-1):
            for j in range(n-1,0-1,-1):
                #this case could be included in below two cases
                if m==1 or n==1:
                    if obstacleGrid[i][j] == 1:
                        return 0
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i==m-1:
                    if j<n-1 and obstacleGrid[i][j+1]==1:
                        grid[i][j] = 0
                        obstacleGrid[i][j] =1
                    else:
                        grid[i][j] = 1
                elif j == n-1:
                    if i<m-1 and obstacleGrid[i+1][j]==1:
                        grid[i][j] = 0
                        obstacleGrid[i][j] =1
                    else:
                        grid[i][j] = 1
                else:
                    grid[i][j] = grid[i+1][j]+grid[i][j+1]
        return grid[0][0]

solution = Solution()
ex1 =  [[0,0,0,0,0],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0]]

ex2 = [[0,0,0,0,1]]

ex4 = [[0,0],
       [0,1]]

ex3 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
print solution.uniquePathsWithObstacles(ex1)
print solution.uniquePathsWithObstacles(ex2)
print solution.uniquePathsWithObstacles(ex3)
print solution.uniquePathsWithObstacles(ex4)

