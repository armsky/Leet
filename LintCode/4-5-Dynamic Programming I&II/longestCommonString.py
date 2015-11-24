"""
Given two strings, find the longest common substring.

Return the length of it.

Example
Given A = "ABCD", B = "CBCE", return 2.

Note
The characters in substring should occur continuously in original string. This is different with subsequence.
"""
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        m = len(A)
        n = len(B)
        dp = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(map(max, dp))

so = Solution()
print so.longestCommonSubstring("ABCDBCE", "CBCE")

