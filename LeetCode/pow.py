"""
Implement pow(x, n).

1.Most naive method, simply multiply x n times:
The time complecity is O(n), but will cause(stack overflow)error

2.Do division before recursive:
x^n = x^n/2 * x^n/2 * x^n%2
Time complexity is O(logN)

NOTE:
1. n might be positive or negetive
2. 0^0 = 1, 0^positive = 0, 0^negetive nonsence
"""
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    # Recursive
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    # Iterative
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        re = 1
        while n:
            if n & 1 == 1:
                re *= x
            x *= x
            n = n >> 1
        return re

solution = Solution()
print solution.pow(0.00001, 2147483647)
print solution.pow(34.00515, -3)
