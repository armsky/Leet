"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        nums = []
        # There would be n! permutations total.
        factorial = [1] * (n+1)
        nums = range(1, n+1) # Create a list [1, n+1]
        for i in xrange(1, n+1):
            factorial[i] = factorial[i-1] * i

        result = ""
        k -= 1
        for i in xrange(n, 0, -1):
            j = k / factorial[i-1]
            k = k % factorial[i-1]
            result += nums.pop(j)

        return result

su = Solution()
print su.getPermutation(1,1)
