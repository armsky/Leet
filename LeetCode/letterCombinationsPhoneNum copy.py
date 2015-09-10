"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        def generate(deep, temp, result, digits, board):
            if deep == len(digits):
                result.append(temp)
                return
            digit = digits[deep]
            for char in board[digit]:
                generate(deep+1, temp+char, result, digits, board)

        result = []
        temp = ""
        deep = 0
        board = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            }
        generate(0, temp, result, digits, board)
        return result

so = Solution()
print so.letterCombinations("23")
