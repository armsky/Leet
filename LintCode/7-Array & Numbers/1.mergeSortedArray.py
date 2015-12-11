"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Have you met this question in a real interview? Yes
Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
"""
class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        t = m+n-1
        m -= 1
        n -= 1
        while m >= 0 and n>= 0:
            if A[m] > B[n]:
                A[t] = A[m]
                m -= 1
            else:
                A[t] = B[n]
                n -= 1
            t -= 1
        # Must be n+1 not n
        for i in range(n+1):
            A[i] = B[i]
        print A
so = Solution()
a = [1,2,3,None, None]
b = [4,5]
so.mergeSortedArray(a, 3, b, 2)
