"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        hashmap = dict()
        for i in range(len(num)):
            hashmap[num[i]] = i
        result = 1
        maxLength = 1
        for i in num:
            upperBound = 1
            lowerBound = 1
            if hashmap.has_key(i):
                temp = i+1
                while hashmap.has_key(temp):
                    del hashmap[temp]
                    upperBound = upperBound +1
                    temp = temp+1
                temp = i-1
                while hashmap.has_key(temp):
                    del hashmap[temp]
                    lowerBound = lowerBound +1
                    temp = temp-1
                if upperBound+lowerBound-1 > maxLength:
                    maxLength = upperBound+lowerBound-1
        result = maxLength
        return result

solution = Solution()
print solution.longestConsecutive([100, 4, 200, 1, 3, 2])


