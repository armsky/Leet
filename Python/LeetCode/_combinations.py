"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):

    def takeKfromN(self, n, k):
        numList = []
        if n == k:
            for i in range(n+1):
                numList.append(i)
            return numList
        elif n < k:
            return None
        else:


