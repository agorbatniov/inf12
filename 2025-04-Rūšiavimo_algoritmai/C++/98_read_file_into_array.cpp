#include <iostream>
#include <fstream>
#include <string>

#define MAX_LINES 224

int main() {
    std::ifstream file("list.txt"); // Open the file
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::string lines[MAX_LINES];
    std::string line;
    int count = 0;
    while (count < MAX_LINES && std::getline(file, line)) {
        lines[count++] = line; // Store each line in the array
    }

    file.close(); // Close the file

    // Output the read lines
    for (int i = 0; i < count; ++i) {
        std::cout << lines[i] << std::endl;
    }
    
    return 0;
}