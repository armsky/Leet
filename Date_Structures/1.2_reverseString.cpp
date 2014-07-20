//
//reverses a null-terminated string
//
#include <string>
#include <iostream>

using namespace std;

void reverse(char* str){
  char* end = str;
  if(str){
    //careful with null string
    while(*end)
      //find the end of the string, which should be null
      ++end;
    //one char back, which is the last non-null char
    --end;

    char tmp;
    while(str < end){
      tmp = *str;
      *str++ = *end;
      *end-- = tmp;
    }
  }
}

int main(){
  char test1[] = "abcdefg";
  char test2[] = "asdfgh";
  char* point1 = test1;
  char* point2 = test2;

  reverse(point1);
  reverse(point2);

  cout << test1 << "//" << test2 << endl;
}
