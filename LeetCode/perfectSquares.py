"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Will have TLE
        import sys
        sqs = []
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        for i in xrange(n/2 +1):
            sqs.append(i*i)
        for i in xrange(0, n+1):
            for j in xrange(len(sqs)):
                if i + sqs[j] <= n:
                    dp[i+sqs[j]] = min(dp[i+sqs[j]], dp[i] + 1)
                #print dp
        return dp[n]

    # Based on Lagrange's Four-Square Theorem (Number theory):
    # every natural number can be represented as the sum of four integer squares.
    def numSquares(self, n):
        import math
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        a = 0
        while a*a <=:
            b = int(math.sqrt(n - a*a))
            if a*a + b*b == n:
                if a!=0 and b!=0:
                    return 2
                elif a==0 or b == 0:
                    return 1
                else:
                    return 0
            a += 1
        return 3


so = Solution()
print so.numSquares(6175)
