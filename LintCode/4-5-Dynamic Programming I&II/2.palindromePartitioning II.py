"""
II.
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Have you met this question in a real interview? Yes
Example
For example, given s = "aab",

Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    # My initial thought
    # O(n^2) space, O(n^2) time
    def minCut(self, s):
        if not s or len(s) <= 1:
            return 0
        n = len(s)
        print n
        # Build palindrome matrix
        # m[i][j]=1 means s[i:j+1] is palindrome
        m = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(i, n):
                print i, j
                if i == j:
                    m[i][j] = 1
                else:
                    m[i][j] = self.is_palindrome(i, j, s)

        # Initialize dp to store min cut
        # dp[i] means in s[0:i] minimum numbers of cuts that satisfy
        dp = []
        for i in range(n+1):
            dp.append(i-1) # Make dp[0] = -1

        for i in range(1, n+1):
            for j in range(0, i):
                if m[j][i-1] == 1:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[n]

    def is_palindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1

    # A modified algorithm
    # O(n^2) time, O(n) space
    # Credit to: https://leetcode.com/discuss/53981/56-ms-python-with-explanation
    def minCut2(self, s):
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]

b = "aac"
so = Solution()
print so.minCut2(a)
