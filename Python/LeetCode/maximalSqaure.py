"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
"""
# dp[x][y] means the bottom right coner (x,y) has the length of largest square
# dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for x in range(m)]
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                if ans < dp[i][j]:
                    ans = dp[i][j]
        return ans * ans
