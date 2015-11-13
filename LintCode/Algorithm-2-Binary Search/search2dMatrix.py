"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview? Yes
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
"""

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not target:
            return False
        M = len(matrix) - 1
        N = len(matrix[0]) - 1

        if target < matrix[0][0] or target > matrix[M][N]:
            return False
        if target > matrix[M][0]:
            X = M
        else:
            l = 0
            r = M
            while r - l > 1:
                m = l + ((r-l) >> 1)
                if target > matrix[m][0]:
                    l = m
                elif target < matrix[m][0]:
                    r = m
                else:
                    return True
            X = l
        l = 0
        r = N
        while l <= r:
            n = l + ((r-l) >> 1)
            if target > matrix[X][n]:
                l = n + 1
            elif target < matrix[X][n]:
                r = n - 1
            else:
                return True
        return False

so = Solution()
print so.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 7)
print so.searchMatrix([[1,2,8,10,16,21,23,30,31,37,39,43,44,46,53,59,66,68,71],[90,113,125,138,157,182,207,229,242,267,289,308,331,346,370,392,415,429,440],[460,478,494,506,527,549,561,586,609,629,649,665,683,704,729,747,763,786,796],[808,830,844,864,889,906,928,947,962,976,998,1016,1037,1058,1080,1093,1111,1136,1157],[1180,1204,1220,1235,1251,1272,1286,1298,1320,1338,1362,1378,1402,1416,1441,1456,1475,1488,1513],[1533,1548,1563,1586,1609,1634,1656,1667,1681,1706,1731,1746,1760,1778,1794,1815,1830,1846,1861]],
        1861)

"""
Test cases:
    1. target smaller than first num or bigger than last num
    2. target bigger than matrix[m][0]

NOTE:
    Three steps:
    1. target bigger that matrix[m][0], jump to step 2
    2. find a position make l < target < r, return l
    3. use case 1 of binary search
"""
