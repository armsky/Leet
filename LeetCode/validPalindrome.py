"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
#Beware: "alphanumric" means it is an alphabetic or number

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s:
            aList = []
            sList = list(s)
            for char in sList:
                if char.isalnum():
                    aList.append(char.lower())

            for i in range(0, len(aList)/2):
                if aList[i] != aList[-(i+1)]:
                    return False
            return True
        else:
            return True

solution = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
#be careful, if the string only has two charaters, the len(list)/2 will give you "1" as result
#which is bad for result
s3 = "ab"
print solution.isPalindrome(s1)
print solution.isPalindrome(s2)
print solution.isPalindrome(s3)

