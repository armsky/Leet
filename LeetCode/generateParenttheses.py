"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution:
    # @param {integer} n
    # @return {string[]}

    # Initial solution, will have TLE
    def generateParenthesis(self, n):
        def insert(n, temp, re):
            if n == 0:
                if temp not in re:
                    re.append(temp)
                return
            insert(n-1, "()"+temp, re)
            insert(n-1, temp+"()", re)
            for i in xrange(len(temp)):
                if temp[i] == "(":
                    insert(n-1, temp[0:i+1]+"()"+temp[i+1:], re)
            return

        re = []
        if n >= 1:
            insert(n-1, "()", re)
            return re
        else:
            return [""]

    # A better solution
    def generateParenthesis(self, n):
        def insert(temp, left, right, re):
            # Handle ")("
            if left > right:
                return
            if left == 0 and right == 0:
                re.append(temp)
                return re
            if left > 0:
                insert(temp+"(", left-1, right, re)
            if right > 0:
                insert(temp+")", left, right-1, re)


        re = []
        if n >= 1:
            insert("", n, n, re)
            return re
        else:
            return [""]
