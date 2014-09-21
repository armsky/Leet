/*
 * Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        int i = 0;
        while (i < path.size()){
          while (path[i] == '/' && i < path.size())
            i++;
          if (i == path.size())
            break;
          //element left bound
          int start = i;
          //element right bound
          while (path[i] != '/' && i < path.size())
            i++;
          int end = i-1;
          string element = path.substr(start, end - start +1);
          if (element == ".."){
            if (stack.size() > 0)
              stack.pop_back();
          }
          else if (element != ".")
            stack.push_back(element);
        }
        if (stack.size() == 0)
          return "/";
        string result;
        for ( int i =0; i < stack.size(); i++){
          result += "/" + stack[i];
        }
        return result;
    }
};

int main(){
  Solution *so = new Solution;
  string path = "/a/./b/../../c/";
  cout << so->simplifyPath(path);
}
