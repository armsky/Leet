/*
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Anwser: paths[i][j] = paths[i-1][j] + paths[i][j-1]
*/

#include <iostream>
#include <vector>
using namespace std;

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

int main(){
  Solution *solution = new Solution();
  cout << solution->uniquePaths(3,7);
  cout << solution->uniquePaths(1,2);
}
