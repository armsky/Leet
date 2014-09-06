/*
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    string convert(string s, int nRows) {
        if (nRows == 1){
          return s;
        }
        string result;
        int diff = 2*(nRows-1);
        //int temp[nRows][s.size()/nRows];
        vector<string> temp(nRows, "");
        for (int i = 0; i < s.size(); i++){
          int n;
          char c = s.at(i);
          if (i < diff) n = (i+diff)%diff;
          else n = i%diff;
          if (n > nRows-1) n = -(n-diff);
          temp[n].push_back(c);
        }
        for (int i = 0; i< nRows; i++){
          result.append(temp[i]);
        }
        return result;
    }
};

int main(){
  Solution *solution = new Solution();
  cout << solution->convert("PAYPALISHIRING", 3);

}
