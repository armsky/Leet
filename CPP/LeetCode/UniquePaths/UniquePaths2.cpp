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
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        
    }
};

class Solution {
public:
    //DP
    int uniquePaths(int m, int n) {
        //MUST initialize this vector!!
        vector<vector<int> > grid(m, vector<int>(n,0));
        for (int i=m-1;i>=0;i--){
          for (int j=n-1;j>=0;j--){
            if (i==m-1 || j==n-1){
              grid[i][j] = 1;
            }else{
              grid[i][j] = grid[i+1][j]+grid[i][j+1];
            }
          }
        }
        return grid[0][0];
    }
    //recursive
    int up_r(int m, int n){
      if (m==1 || n==1) return 1;
      return up_r(m-1,n) + up_r(m,n-1);
    }
    //DP with memory efficiency
    int uniquePaths_2(int m, int n){
      vector<int> grid(n,1);
      for (int i=1; i<m; i++){
        for (int j=1; j<n; j++){
          grid[j] += grid[j-1];
        }
      }
      return grid[n-1];
    }
};
