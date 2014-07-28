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
#include <iostream>
using namespace std;

void reverseWords(string &s);
void reverseWords_2(string &s);
void reverseWords_recursion(string &s);

int main(){
  string s = "the sky is blue";
  reverseWords_2(s);
  cout << s << endl;
  string s1 = " the sky is yellow  ";
  reverseWords_recursion(s1);
  cout << s1 << endl;

  return 0;
}

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
  return;
}

void reverseWords_2(string &s) {
  string ns;
  for (int i = s.size()-1; i >= 0;){
    while (i >= 0 && s[i] == ' ')
      i--;
    if (i < 0)
      break;
    if (!ns.empty())
      ns.push_back(' ');
    string temp;
    while (i >= 0 && s[i] != ' '){
      temp.push_back(s[i--]);
    }
    reverse(temp.begin(), temp.end());
    ns = ns + temp;
  }
  s = ns;
}

void reverseWords_recursion(string &s){
  if (s.empty())
    return;

  while (s[s.size()-1] == ' ')
    s = s.substr(0, s.size()-1);

  int i = s.size();
  string temp;
  while (s[i-1] != ' '){
    temp = s[i-1] + temp;
    i--;
  }

  string rhs = s.substr(0, s.size() - temp.size());
  reverseWords_recursion(rhs);
  s = temp + ' ' + rhs;
}
