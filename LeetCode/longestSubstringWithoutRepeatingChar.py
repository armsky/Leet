"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        re = s[0]
        m = 1
        for i in xrange(1, len(s)):
            if s[i] not in re and s[i] != re[-1]:
                re += s[i]
            else:
                j = re.index(s[i])
                re = re[j+1:] + s[i]
            if len(re) > m:
                m = len(re)
        return m

so = Solution()
print so.lengthOfLongestSubstring("abcabcbbabsdde")
