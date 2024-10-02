// The Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
//                         1  2  3  4  5  6  7   8   9   10  11  12

#include <iostream>
using namespace std;

long long F(int n) {
    if(n <= 2) return 1;
    return F(n-1) + F(n-2);
}

int main() {
  cout << F(8) << "\n";
  return 0;
}
