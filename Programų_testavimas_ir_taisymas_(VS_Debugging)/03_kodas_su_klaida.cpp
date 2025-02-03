#include <iostream>
#include <vector>
using namespace std;

// Funkcija, kuri apskaičiuoja matricos eilučių sumas
vector<int> calculate_row_sums(const vector<vector<int>>& matrix) {
    vector<int> row_sums(matrix.size(), 0);
    
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            row_sums[i] += matrix[i][j];
        }
    }
    
    return row_sums;
}

// Funkcija, kuri randa didžiausią sumą
int find_max_sum(const vector<int>& row_sums) {
    int max_sum = row_sums[0];
    
    for (size_t i = 1; i < row_sums.size(); ++i) {
        if (row_sums[i] < max_sum) {
            max_sum = row_sums[i];
        }
    }
    
    return max_sum;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    vector<int> row_sums = calculate_row_sums(matrix);
    int max_sum = find_max_sum(row_sums);
    
    cout << "Eilučių sumos: ";
    for (int sum : row_sums) {
        cout << sum << " ";
    }
    cout << endl;
    
    cout << "Didžiausia suma: " << max_sum << endl;  # Klaida: neteisinga didžiausia suma
    
    return 0;
}