/*
 * Write an efficient algorithm that searches for a value in an m x n matrix.
 * This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
*/
#include <vector>
using namespace std;

class Solution {
public:
    //regular method.
    bool searchMatrix2(vector<vector<int> > &matrix, int target) {
        int row = matrix.size();
        if (row == 0) return false;
        int col = matrix[0].size();
        for (int i = 0; i < row; i++){
          if ( matrix[i][0] <= target && target <= matrix[i][col-1]){
            for (int j =0; j < col; j++){
              if (matrix[i][j]== target)
                return true;
            }
          }
        }
        return false;
    }

    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        int row = matrix.size();
        if (row == 0) return false;
        int col = matrix[0].size();
        int l = 0;
        int r = row-1;
        int mid;
        for (
    }

};
