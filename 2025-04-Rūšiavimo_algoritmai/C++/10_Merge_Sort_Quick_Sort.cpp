#include <iostream>
#include <vector>

using namespace std;

// Merge Sort funkcijos
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Quick Sort funkcijos
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quick_sort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

// Testavimas
int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    cout << "Originalus masyvas: ";
    for (int num : arr) cout << num << " ";
    cout << endl;

    vector<int> mergeSortedArr = arr;
    merge_sort(mergeSortedArr, 0, mergeSortedArr.size() - 1);
    cout << "Surikiuotas su Merge Sort: ";
    for (int num : mergeSortedArr) cout << num << " ";
    cout << endl;

    vector<int> quickSortedArr = arr;
    quick_sort(quickSortedArr, 0, quickSortedArr.size() - 1);
    cout << "Surikiuotas su Quick Sort: ";
    for (int num : quickSortedArr) cout << num << " ";
    cout << endl;

    return 0;
}
