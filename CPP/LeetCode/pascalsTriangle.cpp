/*Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
#include <vector>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > result;
        if (numRows == 0)
          return result;
        for (int n = 0; n<numRows; n++){
          //Limit the vector size to avoid memory used too much
          vector<int> temp(n+1, 1);
          if (n < 2)
            result.push_back(temp);
          else{
            for (int i = 1; i < n; i++){
              temp[i] = (result[n-1][i-1]+result[n-1][i]);
              cout << temp[i] << "\n";
            }
            result.push_back(temp);
          }
        }
        return result;
    }
};

int main(){
  Solution *solution = new Solution;
  vector<vector<int> > result = solution->generate(3);
  }
