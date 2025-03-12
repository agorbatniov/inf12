#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int SIZE = 1000;

// Funkcija atsitiktiniø skaièiø generavimui
void generateRandomNumbers(int arr[], int size) {
    srand(time(0)); // Inicijuojame atsitiktiniø skaièiø generatoriø
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000000 + 1; // Sugeneruojame skaièius nuo 1 iki 1000000
    }
}

int main() {
    int arr[SIZE];

    // Kvieskime funkcijà, kad sugeneruotø skaièius
    generateRandomNumbers(arr, SIZE);

    // Iðvedame pirmus 10 sugeneruotø skaièiø
    cout << "Sugeneruoti skaièiai: ";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
