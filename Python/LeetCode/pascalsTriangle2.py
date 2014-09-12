"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            result[i] = 1
            if i > 1:
                for j in range(i-1, 0, -1):
                    if j > 0:
                        result[j] = result[j] + result[j-1]
        return result

solution = Solution()
print solution.getRow(4)
print solution.getRow(0)
