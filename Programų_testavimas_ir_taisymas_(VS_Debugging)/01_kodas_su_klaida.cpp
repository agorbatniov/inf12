#include <iostream>
using namespace std;

int calculate_sum(int a, int b) {
    int result = a - b;  // Klaida: turėtų būti a + b
    return result;
}

int main() {
    cout << calculate_sum(5, 3) << endl;
    return 0;
}