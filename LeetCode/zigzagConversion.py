"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

0   6
1  57
2 4 8
3   9

"""

class Solution:
    # @return a string
    def convert(self, s, nRows):
        #Remeber extreme situation !!!
        if nRows == 1:
            return s
        temp = [[] for x in range(nRows)]
        size = len(s)
        diff = 2*(nRows-1)
        result = ''
        for i in range(len(s)):
            char = s[i]
            if i<diff:
                n = (i+diff)%diff
            else:
                n = i%diff
            if n >= nRows:
                n = -(n-diff)
            print i, n, char
            temp[n].append(char)
        for n in range(len(temp)):
            result += ''.join(temp[n])
        return result

solution = Solution()
print solution.convert("PAYPALISHIRING", 3)
print solution.convert("ABCdef", 2)
print solution.convert("A", 1)

