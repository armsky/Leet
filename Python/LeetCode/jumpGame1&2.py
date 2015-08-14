"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution:
    # @param {integer[]} nums
    # @return {boolean}

    # Naive solution by using a queue, will have TLE
    def canJump(self, nums):
        if not nums:
            return False
        # If nums only contains [0] should also return True
        elif len(nums) == 1 and nums[0] == 0:
            return True
        import Queue
        jump = Queue.Queue()
        jump.put((0, nums[0]))
        while not jump.empty():
            pos, val = jump.get()
            print pos, val
            if val > 0:
                for i in xrange(1, val+1):
                    new_pos = pos + i
                    if new_pos >= len(nums) -1:
                        return True
                    else:
                        jump.put((new_pos, nums[new_pos]))
        return False

    # DP solution
    # Notice that in index i, the range that could jump to is [i:i + nums[i]]
    def canJump(self, nums):
        maxindex = 0
        for i in xrange(len(nums)):
            if i > maxindex:
                return False
            elif maxindex >= len(nums) - 1:
                return True
            else:
                maxindex = max(maxindex, i + nums[i])

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
    # @param {integer[]} nums
    # @return {integer}

    # NOTE instead of tracking the length it can jump, track the times of jump that will
    # reach to the last index
    def jump(self, nums):
        cur_length = 0
        njump = 0
        i = 0
        while cur_length < len(nums) -1:
            last_length = cur_length
            for i in xrange(i, last_length+1):
                cur_length = max(cur_length, i + nums[i])
            njump += 1
            if cur_length == last_length:
                return -1
        return njump



so = Solution()
print so.canJump([2,5,0,0])
