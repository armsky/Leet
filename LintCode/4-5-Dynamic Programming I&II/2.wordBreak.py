"""
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

Example
Given s = "lintcode", dict = ["lint", "code"].

Return true because "lintcode" can be break as "lint code".
"""

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        if not dict:
            return not s
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        # Good way to reduce time
        max_word_len = max([len(w) for w in dict])
        for i in range(1, n+1):
            for j in range(1, min(i, max_word_len) + 1):
                if dp[i-j] == True and s[i-j:i] in dict:
                    dp[i] = True
                    break
                print dp, i, j
        return dp[len(s)]

dict = {
        'leet':'1',
        'code':'1'}
so = Solution()
print so.wordBreak("leetcode", dict)
