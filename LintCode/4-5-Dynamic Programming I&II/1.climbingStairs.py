"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
"""

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 1
        dp = [0]
        for i in range(1, n+1):
            if i == 1:
                dp.append(1)
            elif i == 2:
                dp.append(2)
            else:
                dp.append(dp[i-1] + dp[i-2])
        return dp[n]
