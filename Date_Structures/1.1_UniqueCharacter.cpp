//
//Detemine if a string has all unique characters.
//
#include <iostream>

using namespace std;

bool isUnique(string test_string){
// This will take O(n2) time and O(1) space
  for (int i = 0; i < test_string.size(); ++i){
    for (int j = i+1; j < test_string.size(); ++j){
      if (test_string[i] == test_string[j])
        return false;
      }
    }
  return true;
}

bool isUnique2(string test_string){
// This will take O(n) time and O(1) space.
// Assume the string is a ASCII string.
}

int main(){
  const string aString = "asdfgsd";
  const string bString = "asdfghj";

  cout << aString << "\n";
  cout << bString << "endl" << "\n";
  cout << "DONE\n";


if (isUnique(aString))
  cout << aString << " has all unique characters.\n";
else
  cout << aString << " does not have all unique characters.\n";

if (isUnique(bString))
  cout << bString << " has all unique characters.\n";
else
  cout << bString << " does not have all unique characters.\n";
}




