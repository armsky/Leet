"""
Given a string s and a dictionary of words dict, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict or not s:
            return False
        dp = [False] * (len(s) +1)
        dp[0] = True

        for i in xrange(1, len(s)+1):
            for k in xrange(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]

