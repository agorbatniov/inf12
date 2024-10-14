#include <iostream>
#include <vector>

int binary_search(const std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Randame vidurį
        
        if (arr[mid] == target)
            return mid;  // Elementas rastas
        
        else if (arr[mid] < target)
            left = mid + 1;  // Ieškome dešinėje pusėje
        
        else
            right = mid - 1;  // Ieškome kairėje pusėje
    }
    
    return -1;  // Elementas nerastas
}

int main() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11, 13};
    int target = 7;
    
    int result = binary_search(arr, target);
    if (result != -1) {
        std::cout << "Elementas rastas indeksu " << result << std::endl;
    } else {
        std::cout << "Elementas nerastas" << std::endl;
    }
    
    return 0;
}
