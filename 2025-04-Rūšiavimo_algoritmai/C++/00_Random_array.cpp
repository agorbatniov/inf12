#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int SIZE = 1000;

// Funkcija atsitiktini� skai�i� generavimui
void generateRandomNumbers(int arr[], int size) {
    srand(time(0)); // Inicijuojame atsitiktini� skai�i� generatori�
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000000 + 1; // Sugeneruojame skai�ius nuo 1 iki 1000000
    }
}

int main() {
    int arr[SIZE];

    // Kvieskime funkcij�, kad sugeneruot� skai�ius
    generateRandomNumbers(arr, SIZE);

    // I�vedame pirmus 10 sugeneruot� skai�i�
    cout << "Sugeneruoti skai�iai: ";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
