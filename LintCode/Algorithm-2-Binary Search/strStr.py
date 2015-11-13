"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Have you met this question in a real interview? Yes
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""

class Solution:
    def strStr(self, source, target):
        if target is None or source is None:
            return -1
        if not target == 0:
            return 0

        for i in range(len(source)):
            if source[i] == target[0]:
                for j in range(1, len(target)):
                    x = i + j
                    print x, j
                    if source[x] != target[j]:
                        break
                    if j == len(target) - 1:
                        return i
        return -1

so = Solution()
print so.strStr(None, "bcd")

"""
Test cases:
    1. ("", ""), should return 0
    2. ("", "s"), should return -1
    3. ("s", ""), should return 0
    4. ("abcdabcdefg", "bcd"), should return 1, the first available answer.
    5. (None, "a"), should return -1
    6. ("a", None), should return -1

NOTE: not "" will give True in Python!
"""
