#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

void bubbleSort(int arr[], int n) {
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped)
            break;
    }
}

int main() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90, 15, 5, 6 };
    int n = sizeof(arr) / sizeof(arr[0]);

    // Pradedame laiko matavim�
    auto start = high_resolution_clock::now();

    bubbleSort(arr, n);

    // Baigiame laiko matavim�
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    // I�vedame i�r��iuot� masyv�
    cout << "I�r��iuotas masyvas: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    // I�vedame veikimo laik� mikrosekund�mis
    cout << "Vykdymo laikas (Bubble Sort): " << duration.count() << " ms" << endl;

    return 0;
}
