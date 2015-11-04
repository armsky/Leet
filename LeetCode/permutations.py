"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def create(nums, re, temp):
            if not nums:
                re.append(temp)
                return
            num = nums[0]
            for i in xrange(len(temp)+1):
                new_temp = temp[:i] + [num] + temp[i:]
                create(nums[1:], re, new_temp)

        re = []
        create(nums[1:], re, [nums[0]])
        return re

    # A neater solution by other people
    def permute_(self, nums):
        if not nums:
            return []
        elif len(nums) == 1:
            return [nums] # Not nums but [nums] here
        re = []
        for i in xrange(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                re.append([nums[i]] + j)
        return re

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        elif len(nums) == 1:
            return [nums]
        nums.sort()
        re = []
        pre = None
        for i in xrange(len(nums)):
            if nums[i] == pre:
                continue
            pre = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                re.append([nums[i]] + j)
        return re

    if not nums:
            return []
        nums.sort()
        def create(nums, re, temp):
            if not nums:
                re.append(temp)
                return
            num = nums[0]
            for i in xrange(len(temp)+1):
                if i < len(temp) and temp[i] == num:
                    continue
                else:
                    new_temp = temp[:i] + [num] + temp[i:]
                    create(nums[1:], re, new_temp)

        re = []
        create(nums[1:], re, [nums[0]])
        return re



su = Solution()
print su.permuteUnique([3,3,0,0,2,3,2])
