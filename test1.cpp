#include <iostream>
using namespace std;

int main(int argc, const char *argv[])
{
  std::cout << "Hello World\n";
  int value = 0;
  int sum = 0;
  while (cin >> value){
    sum += sum+value;
  }
  cout << "sum is " << sum << endl;
  return 0;
}
