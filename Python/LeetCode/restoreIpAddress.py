"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

NOTE: This is a Combination question, use DFS
"""
class Solution:
    # @param s, a string
    # @return a list of strings

    def isValid(self, s):
        num = int(s)
        if num != 0 and s[0] == '0':
            return False
        if num == 0 and len(s) >1 :
            return False
        if 0<= num <= 255:
            return True
        else:
            return False

    def dfs(self, s, temp, result, partition=0):
        if len(temp.split('.'))>4:
            return
        if partition == 3 and self.isValid(s):
            result.append(temp+s)
            return
        #In Python, there is no For Lop could hold two conditions like Java or C++
        i = 1
        while i < 4 and i < len(s):
            subStr = s[:i]
            if self.isValid(subStr):
                self.dfs(s[i:], temp+subStr+'.', result, partition+1)
            i+=1

    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        result = []
        self.dfs(s, '', result, 0)
        return result

solution = Solution()
print solution.restoreIpAddresses("25525511135")
print solution.restoreIpAddresses("010010")



