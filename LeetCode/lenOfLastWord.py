"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""
def lengthOfLastWord(s):
    sl = s.split(' ')
    print sl
    for i in xrange(-1, -len(sl)-1, -1):
        if sl[i] is not "":
            return len(sl[i])
    else:
        return 0
s = " a "
print lengthOfLastWord(s)
