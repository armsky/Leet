//Given an input string, reverse the string word by word.

//For example,
//Given s = "the sky is blue",
//return "blue is sky the".

//click to show clarification.

//Clarification:
//What constitutes a word?
//A sequence of non-space characters constitutes a word.
//Could the input string contain leading or trailing spaces?
//Yes. However, your reversed string should not contain leading or trailing spaces.
//How about multiple spaces between two words?
//Reduce them to a single space in the reversed string.
//

#include <string>
using namespace std;

class Solution {
  public:
    void reverseWords(string &s) {
      int l = s.size()-1;
      int start = 0;
      while (l >= 0){
        int size = s.size();
        if (s[size-1] == ' '){
          l--;
          s = s.substr(0, size-1);
          continue;
        }

        string temp = "";
        int count = 0;
        while (s[size-1] != ' ' && l >= 0){
          temp = s[size-1] + temp;
          size--;
          l--;
          count++;
        }
        temp += ' ';
        count++;
        string lhs = s.substr(0, start);
        string rhs = s.substr(start, size - start);
        start += count;
        s = lhs + temp + rhs;
      }
      s = s.substr(0, s.size()-1);
    }
};

