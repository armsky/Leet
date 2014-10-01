"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        result = ""
        if len(strs) == 0:
            return result
        for i in range(len(strs[0])):
            char = strs[0][i]
            try:
                for j in range(len(strs)):
                    if strs[j][i] != char:
                        return result
            except:
                return result
            result += char
        return result
