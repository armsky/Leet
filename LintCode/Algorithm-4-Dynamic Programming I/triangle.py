"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Example
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return None
        dp = [0] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif i == j:
                    dp[j] = dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
        return min(dp)

so = Solution()
print so.minimumTotal([[-1],[2,3],[1,-1,-3]])
