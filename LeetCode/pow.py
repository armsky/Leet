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
    def pow(self, x, n):
        if x==0:
            if n>0:
                return 0
            elif n==0:
                return 1
            else:
                return "some ERROR"
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            #becareful the "self" here
            if n>0:
                return self.power(x,n)
            else:
                return 1.0/self.power(x,-n)
    #becareful the "self" here
    def power(self, x, n):
        if n==0:
            return 1
        v = self.power(x, abs(n/2))
        if n%2 == 1:
            return v*v*x
        else:
            return v*v

solution = Solution()
print solution.pow(0.00001, 2147483647)
print solution.pow(34.00515, -3)
