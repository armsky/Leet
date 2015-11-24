"""
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Have you met this question in a real interview? Yes
Example
For [5, 4, 1, 2, 3], the LIS  is [1, 2, 3], return 3

For [4, 2, 4, 5, 3, 7], the LIS is [4, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)

Clarification
What's the definition of longest increasing subsequence?

    * The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

    * https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] >= dp[-1]:
                dp.append(nums[i])
            elif nums[i] < dp[0]:
                dp[0] = nums[i]
            else:
                dp[self.insert(dp, nums[i])] = nums[i]

        return len(dp)

    def insert(self, dp, target):
        i = 0
        j = len(dp) -1
        while i < j-1:
            m = (i+j)/2
            if dp[m] > target:
                j = m
            elif dp[m] <= target:
                i = m
        return j

so = Solution()
a = [10,1,11,2,12,3,11]
print so.longestIncreasingSubsequence(a)
