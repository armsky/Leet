"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for n in range(numRows):
            temp = []
            if n == 0:
                temp.append(1)
            elif n == 1:
                temp = [1,1]
            else:
                for i in range(n+1):
                    if i == 0:
                        temp.append(1)
                    elif i != n:
                        temp.append(result[n-1][i-1] + result[n-1][i])
                    else:
                        temp.append(1)
            result.append(temp)
        return result

solution = Solution()
print solution.generate(5)

