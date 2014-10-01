/*
 * Write a function to find the longest common prefix string amongst an array of strings.
 */
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        string result;
        if (strs.size() == 0) return result;
        for (int i = 0; i <= strs[0].size(); i++){
          char c = strs[0][i];
          for (int j = 0; j <= strs[j].size(); j++){
            if (i >= strs[j].size()) return result;
            if (strs[j][i] != c) return result;
            result += c;
          }
        }
        return result;
    }
};

int main(){
  vector<string> strs;
  strs.push_back("a");
  Solution *so = new Solution;
  cout << so->longestCommonPrefix(strs);
 }
