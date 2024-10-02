#include <iostream>
using namespace std;

long long fakt(int n) {
    if (n == 0) return 1;
    return n * fakt(n-1);
}

int main() {
  cout << fakt(5) << "\n";
  return 0;
}
