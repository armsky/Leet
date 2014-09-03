/*
 * Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

Reminder: Please do not use nested vectors if the size of your storage is known ahead of time.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int> > grid(m, vector<int>(n,0));
        for (int i=m-1; i>=0; i--){
          for (int j=n-1; j>=0; j--){
            if (obstacleGrid[i][j] == 1){
              grid[i][j] = 0;
            }else if(i == m-1){
              if(j < n-1 & obstacleGrid[i][j+1] ==1){
                grid[i][j] = 0;
                obstacleGrid[i][j] = 1;
              }else{
                grid[i][j] = 1;
              }
            }else if (j == n-1){
              if (i < m-1 & obstacleGrid[i+1][j] ==1){
                grid[i][j] = 0;
                obstacleGrid[i][j] = 1;
              }else{
                grid[i][j] = 1;
              }
            }else{
              grid[i][j] = grid[i+1][j] + grid[i][j+1];
            }
          }
        }
        return grid[0][0];
    }
};

int main(){
    Solution *solution = new Solution();
    vector<vector<int> > ex1(4, vector<int> (5,0));
    ex1[1][4] = 1;
    ex1[2][3] = 1;
    ex1[3][2] = 1;
    //{{0,0,0,0,0},{0,0,0,0,1},{0,0,0,1,0},{0,0,1,0,0}};
    cout << solution->uniquePathsWithObstacles(ex1);
}

