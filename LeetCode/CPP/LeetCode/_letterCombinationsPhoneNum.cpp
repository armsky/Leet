"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
digidic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        result = []
        charList = []
        if digits == None:
            return result
        for digit in digits:
            if digit != '0' and digit != '1':
                charList.append(digidic.get(digit))
        for chars in charList:
            for char in chars:

