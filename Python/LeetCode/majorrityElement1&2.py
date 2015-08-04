"""
1.
Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}

    # Hash table, O(n) time, O(n) space
    def majorityElement(self, nums):
        table = {}
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        major = 0
        for key, value in table.iteritems():
            if value > major:
                major = value
                result = key
        return result

    # Moore's voting algorithm
    # O(n) time, O(1) space
    def majorityElement(self, nums):
        candidate = None
        count = 1
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1
        return candidate

"""
2.
Given an integer array of size n, find all elements that appear more than [n/3] times. The algorithm should run in linear time and in O(1) space.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}

    # Only Moore could be possible
    # Since there could exist at most two majority numbers, keep track of them two
    def majorityElement2(self, nums):
        count1 = count2 = 0
        can1, can2 = None, None
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1 = num
                count1 = 1
            elif count2 == 0:
                can2 = num
                count2 =1
            else:
                count1 -= 1
                count2 -= 1
            print (can1, can2), count1, count2
        size = len(nums)
        return [n for n in (can1, can2) if n is not None and nums.count(n) > size/3]

so = Solution()
print so.majorityElement2([0,0,0])
