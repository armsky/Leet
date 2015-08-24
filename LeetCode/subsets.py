"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = [[]]
        S.sort()
        for n in S:
            for i in result:
                temp = result[i][:]
                temp.append(n)
                result.append(temp)
                print result
        return result

solution = Solution()
solution.subsets([1,2,3])

"""
The output is like:
[[], [1]]
[[], [1], [2]]
[[], [1], [2], [1, 2]]
[[], [1], [2], [1, 2], [3]]
[[], [1], [2], [1, 2], [3], [1, 3]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

NOTE:
.sort() method of lists sorts the list in place, while sorted() creates a new list. 
"""
