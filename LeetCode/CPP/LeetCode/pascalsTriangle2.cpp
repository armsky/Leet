/*
 * Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
      vector<int> result(1,1);
      if (rowIndex == 0)
        return result;
      for (int i = 1; i <= rowIndex; i++){
        result.push_back(1);
        for (int j = i-1; j >=1; j--){
          result[j] = result[j] + result [j-1];
        }
      }
      return result;
    }
};

int main(){
}
