"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import sys
        int_str = ""
        mark = []
        for i in range(len(str)):
            c = str[i]
            if c not in "0123456789":
                if not int_str:
                    if c == ' ':
                        pass
                    elif c == '+':
                        if i < len(str) - 1 and str[i+1] not in "0123456789":
                            return 0
                        else:
                            pass
                    elif c == '-':
                        int_str += c
                    else:
                        return 0
                else:
                    break
                    #if not mark:
                    #    mark.append(i)
                    #if i - mark[-1] > 1:
                    #    return 0
                    #else:
                    #    mark.append(i)
                    #if i < len(str) - 1 and str[i+1] in "0123456789":
                    #    return 0
            else:
                int_str += c
        if int_str == '-' or not int_str:
            return 0
        #if int(int_str) > sys.maxint:
        #    return sys.maxint
        #if int(int_str) < -sys.maxint -1:
        #    return -sys.maxint -1
        # To fit LeetLode
        if int(int_str) > 2147483647:
            return 2147483647
        if int(int_str) < -2147483648:
            return -2147483648
        return int(int_str)

so = Solution()
print so.myAtoi('-1')
print so.myAtoi('   3')
print so.myAtoi(' 3 5')
print so.myAtoi('9223372036854775808   ')
print so.myAtoi('   4   ')
print so.myAtoi('     ')
print so.myAtoi('')
print so.myAtoi('-')
print so.myAtoi('+-2')
print so.myAtoi('  -0012a42')
print so.myAtoi(' b11228552307')


"""
Test cases:
    1. '-1', '+1'
    2. really big number
    3. leading spaces before digits should ignore
    4. None or only spaces -> 0
    5. not a valid input (char in digits) -> 0
    6. Only has '-' or '-     ' -> 0
    7. Has like '+-2' -> 0
    8. "  -0012a42" -> -12
"""
