/*
 * Implement pow(x, n).

1.Most naive method, simply multiply x n times:
The time complecity is O(n), but will cause(stack overflow)error

2.Do division before recursive:
x^n = x^n/2 * x^n/2 * x^n%2
Time complexity is O(logN)

NOTE:
1. n might be positive or negetive
2. 0^0 = 1, 0^positive = 0, 0^negetive nonsence
*/

#include <iostream>
using namespace std;

class Solution {
public:
    double pow(double x, int n) {
      if (n==0) return 1;
      if (n==1) return x;
      if (n>0){
        return power(x, n);
      }else{
        return 1.0/power(x, -n);
      }
    }

    double power(double x, int n){
      if (n==0) return 1;
      double v = power(x, abs(n/2));
      if (n%2 == 1){
        return v*v*x;
      }else{
        return v*v;
      }
    }
};

int main(){
  Solution *solution = new Solution;
  cout << solution->pow(0.00001, 2147483647);
  cout << solution->pow(34.00515, -3);
}
