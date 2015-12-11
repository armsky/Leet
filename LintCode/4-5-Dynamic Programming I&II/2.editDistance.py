"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

`Insert a character
`Delete a character
`Replace a character

Example
Given word1 = "mart" and word2 = "karma", return 3.
"""

class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        if word2 == word1[::-1]:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m = len(word1)
        n = len(word2)
        dp = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]

so = Solution()
so.minDistance( 'sea', 'ate')

"""
Test Case:
    1. 'a','a' -> 0
    2. 'ab','a' -> 1
    3. 'sea', 'ate' -> 3

"""

