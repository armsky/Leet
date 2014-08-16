"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        rowNum = len(matrix)
        colNum = len(matrix[0])
        count = rowNum * colNum
        #trueMatrix = [[True]*rowNum]*colNum
        #This is wrong, it will copy [True]*3 (which is an object) three times
        #if later use tureMatrix[0][0], it will manipulate 3 element not 1 !!!
        trueMatrix = [[True]*colNum for not_used_variable in range(rowNum)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        i = 0
        j = 0
        index = directions[0]
        while count > 0:
            try:
                while trueMatrix[i][j]:
                    result.append(matrix[i][j])
                    print "insert "+ str(matrix[i][j])
                    trueMatrix[i][j] = False
                    print trueMatrix


                    i = i + index[0]
                    j = j + index[1]
                    count = count-1
                    print "count is " + str(count)

                    #python allow index=-1, which means last element
                    #we need to escape from this
                    if j < 0:
                        j = 0
                        break
                    print str(i) + str(j)
            except IndexError:
                print "out of range"
                i = i - index[0]
                j = j - index[1]
                print str(i) + str(j)
            if index == directions[-1]:
                index = directions[0]
                print "index is " + str(index)
            else:
                index = directions[directions.index(index)+1]
                print "index is " + str(index)
            i = i + index[0]
            j = j + index[1]
            print str(i) + str(j)
            print trueMatrix

        return result


solution = Solution()
test =[
 [ 1, 2, 3 ],
 [10,11, 4 ],
 [ 9,12, 5 ],
 [ 8, 7, 6 ]
]
print solution.spiralOrder(test)


