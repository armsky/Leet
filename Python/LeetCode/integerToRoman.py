"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = ""
        while num >= 1000:
            roman += 'M'
            num -= 1000
        while num >= 900:
            roman += 'CM'
            num -= 900
        while num >= 500:
            roman += 'D'
            num -= 500
        while num >= 400:
            roman += 'CD'
            num -= 400
        while num >= 100:
            roman += 'C'
            num -= 100
        while num >= 90:
            roman += 'XC'
            num -= 90
        while num >= 50:
            roman += 'L'
            num -= 50
        while num >= 40:
            roman += 'XL'
            num -= 40
        while num >= 10:
            roman += 'X'
            num -= 10
        if num == 9:
            roman += 'IX'
            return roman
        while num >= 1:
            if num >= 5:
                roman += 'V'
                num -= 5
            elif num == 4:
                roman += 'IV'
                num -= 4
            else:
                roman += 'I'
                num -= 1
        return roman








