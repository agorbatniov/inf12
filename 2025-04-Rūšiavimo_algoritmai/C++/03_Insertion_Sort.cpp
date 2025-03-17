#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main3() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90, 15, 5, 6 };
    int n = sizeof(arr) / sizeof(arr[0]);

    // Pradedame laiko matavimà
    auto start = high_resolution_clock::now();

    insertionSort(arr, n);

    // Baigiame laiko matavimà
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    // Iðvedame iðrûðiuotà masyvà
    cout << "Iðrûðiuotas masyvas: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    // Iðvedame veikimo laikà mikrosekundëmis
    cout << "Vykdymo laikas (Insertion Sort): " << duration.count() << " ms" << endl;

    return 0;
}
