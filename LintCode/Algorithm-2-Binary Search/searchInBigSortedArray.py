"""
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

If you accessed an inaccessible index, ArrayReader.get would return -1.

Return -1, if the number doesn't exist in the array.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.
"""

"""
Definition of ArrayReader:
"""
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
        if index < len(a):
            return a[index]
        else:
            return -1

class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        if not target:
            return -1
        #while reader.get(r) < target:
        #    l = r
        #    r *= 2
        index = 1
        while reader.get(index-1) < target:
            if reader.get(index-1) != -1:
                index *= 2
            else:
                break

        l = 0
        r = index

        while r > l:
            m = (r+l)/2
            if reader.get(m) < target:
                l = m + 1
            else:
                r = m
        if reader.get(l) == target:
            return l
        else:
            return -1

so = Solution()
reader = ArrayReader()
a = []
for i in range(1024):
    a.append(i*2)
print so.searchBigSortedArray(reader, 200)
print a[528]

"""
Test cases:
    1.([1,1,1,1,2,2,3,4], 4)
    2.([4,5,9,9,12,13,14,15,15,18], 10)

NOTE: Use Binary Search case 1. find the only element equals to target. At last, r will always in the left of right.
        But, do a judgement at last:
        1. the target bigger than biggest element in list, return l (len of A)
        2. target < left, return l+1
        3. right < target < left, return l
"""
