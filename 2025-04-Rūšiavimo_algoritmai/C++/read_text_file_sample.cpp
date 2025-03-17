#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {

	string filename = "C:\\Users\\Aleksandr K\\Downloads\\test.txt";

	ifstream file(filename);  // Open the file
	if (!file.is_open()) {
		cout << "Error: Could not open the file " << filename << endl;
		return 1;
	}

	vector<string> lines;  // Vector to store lines
	string line;

	while (getline(file, line)) {  // Read each line
		lines.push_back(line);
	}

	file.close();  // Close the file


	for (size_t i = 0; i < lines.size(); i++)
	{
		cout << lines[i] << endl;
	}

	return 0;
}
