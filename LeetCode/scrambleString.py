"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Ideas: string S1 and S2, if they are scramble, patition them at any postion as s11, s12,
and s21, s22. There must be s12 and s21 are scramble AND s11 and s22 are scramble;
OR s11,s21 are scramble AND s12 and s22 are scrable
"""

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        #print s1, s2

        if len(s1) != len(s2):
            return False
        size = len(s1)
        #extreme situation 1: s1 and s2 are only one character
        if size == 1:
            if s1[0] == s2[0]:
                return True
            else:
                return False
        #extreme situation 2: if s1 and s2 are empty
        if size == 0:
            return False
        #use sort() might need too much time
        #if ''.join(sorted(s1)) != ''.join(sorted(s2)):
        #    return False
        chars = [0 for x in range(26)]
        for i in range(size):
            chars[ord(s1[i])-ord('a')] +=1
            chars[ord(s2[i])-ord('a')] -=1
        for num in chars:
            if num != 0:
                return False
        for i in range(size):
            if i >0:
                s11, s12 = s1[:i], s1[i:]
                s21, s22 = s2[:i], s2[i:]
                #print "s11, s12="+s11 + " " + s12
                #print "s21, s22="+s21 + " " + s22

                if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                    return True
                #IMPORTANT!!!
                s21, s22 = s2[:size-i], s2[size-i:]
                if self.isScramble(s11, s22) and self.isScramble(s12, s21):
                    return True
        else:
            return False

solution = Solution()
print solution.isScramble("ccbbcaccbccbbbcca", "ccbbcbbaabcccbccc")
print solution.isScramble("abb", "bba")
print solution.isScramble("pcighfdjnbwfkohtklrecxnooxyipj", "npodkfchrfpxliocgtnykhxwjbojie")
