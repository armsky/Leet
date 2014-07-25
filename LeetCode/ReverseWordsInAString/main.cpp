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

#include <vector>
#include <string>
using namespace std;

class Solution {
  public:
    void reverseWords(string &s) {
      char ss[100];
      strcpy(ss, s.c_str());
      char* start = ss;
      vector<string> v_string;
      vector<char> v_char;
      for(int i = 0; i < sizeof(s); i++){
        if(ss[i] == " "){
          if(v_char.size() != 0){
            v_string.push_back(string(v_char.begin(),v_char.end()));
            v_char.clear();
          }
        }else{
          v_char.push_back(ss[i]);
        }
      }
    }
};
