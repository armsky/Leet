"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
[0,0,0,1,0,3]
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        l = len(digits)
        total = 0
        for i in range(l):
            num = digits[i]
            value = 10**(l-1-i) * num
            total = total+value
        total = total+1
        totalStr = str(total)
        result = []
        for digit in totalStr:
            result.append(int(digit))
        return result

solution = Solution()
print solution.plusOne([0,0,0,0,1,0,3])

