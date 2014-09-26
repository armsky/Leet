"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        nums = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    nums[0][0] = grid[0][0]
                elif i == 0:
                    nums[i][j] = grid[0][j] + nums[0][j-1]
                elif j == 0:
                    nums[i][j] = grid[i][0] + nums[i-1][0]
                else:
                    nums[i][j] = grid[i][j] + min(nums[i-1][j], nums[i][j-1])
                print  nums[i][j]
        return nums[row-1][col-1]

so = Solution()
so.minPathSum([[1,2],[1,1]])
