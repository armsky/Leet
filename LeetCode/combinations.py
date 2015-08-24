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
        result = []
        stack = []
        level = 1
        self.get_combination(n, k, level, stack, result)
        return result

    def get_combination(self, n, k, level, stack, result):
        if len(stack) == k:
            # Must make a copy of stack and append it to result
            result.append(list(stack))
            return
        for i in xrange(level, n+1):
            stack.append(i)
            self.get_combination(n, k, i+1, stack, result)
            stack.pop()

so = Solution()
print so.combine(1, 1)
