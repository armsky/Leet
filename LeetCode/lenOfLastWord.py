"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""
def lengthOfLastWord(self, s):
    sl = s.split(' ')
    while sl:
        if not sl[-1]:
            sl.pop()
        else:
            return len(sl[-1])

    return 0
