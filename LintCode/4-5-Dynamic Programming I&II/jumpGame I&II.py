"""
I.
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

Note
This problem have two method which is Greedy and Dynamic Programming.
The time complexity of Greedy method is O(n).
The time complexity of Dynamic Programming method is O(n^2).
"""

"""
II.
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A:
            return False
        n = len(A)
        dp = [False] * n
        dp[0] = True
        for i in range(n-1): # If i reachs to n-1, means can jump to the last position
            if dp[i] == True:
                num = A[i]
                dp[i:i+num] = [True] * num
            else:
                return False
        return True

    def jump(self, A):
        # This will have TLE
        import sys
        n = len(A)
        dp = [sys.maxint] * n
        dp[0] = 0
        for i in range(n):
            num = A[i]
            for j in range(i+1, min(i+1+num, n)):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]

    def jump_modified(self, A):
        import sys
        n = len(A)
        dp = [sys.maxint] * n
        dp[0] = 0
        for i in range(1, n):
            dp[i] = sys.maxint
            for j in range(i):
                if dp[j] != sys.maxint and A[j] + j >= i:
                    dp[i] = dp[j]+1
                    break
        return dp[-1]

# Test Case:
A = [1,0]
B = [11,15,28,53,3]
so = Solution()
print so.jump_modified(A)
print so.jump_modified(B)

