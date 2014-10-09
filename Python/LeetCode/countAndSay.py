"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

class Solution:
    # @return a string
    def countAndSay(self, n):
        k = 1
        result = '1'
        while k < n:
            j = 0
            count = 1
            temp = ''
            result = result +"#"#avoid corner issue
            for i in range(1,len(result)):
                if result[i] == result[j]:
                    count += 1
                else:
                    temp = temp + str(count) + str(result[j])
                    j = i
                    count =1
            result = temp
            k += 1
        return result

so = Solution()
print so.countAndSay(6)
