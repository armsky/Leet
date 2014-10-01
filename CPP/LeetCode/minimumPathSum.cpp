/*
 * Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
*/

#include <vector>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
        int row = grid.size();
        int col = grid[0].size();
        vector<vector<int> > num(row, vector<int>(col,0));

        for (int i=0; i < row; i++){
          for (int j=0; j < col; j++){
            if (i==0 && j==0)
              num[i][j] = grid[0][0];
            else if (i == 0)
              num[i][j] = grid[0][j] + num[0][j-1];
            else if (j == 0)
              num[i][j] = grid[i][0] + num[i-1][0];
            else
              num[i][j] = grid[i][j] + min(num[i-1][j], num[i][j-1]);
            cout << to_string(num[i][j]);
          }
        }
        return num[row-1][col-1];
    }
};

int main(){
  Solution *so = new Solution;
  vector<vector<int> > grid;
  vector<int> list1;
  list1.push_back(1);
  list1.push_back(2);
  vector<int> list2(2, 1);
  grid.push_back(list1);
  grid.push_back(list2);
  so->minPathSum(grid);
}
