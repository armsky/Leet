"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""
import collections

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        # Counter is a subclass of dict
        # List cannot be hashed but tuple can be
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)

so = Solution()
print so.anagrams(["dog", "cat", "god"])
