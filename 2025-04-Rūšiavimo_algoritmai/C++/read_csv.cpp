#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

// Struct to hold student data
struct Student {
    string firstName;
    string lastName;
    string subject;
    int grade;
};

// Function to read CSV file and store data into an array
vector<Student> readCSV(const string& filename) {
    vector<Student> students;
    ifstream file(filename);
    string line;
    
    // Skip the header line
    getline(file, line);

    // Read the rest of the file
    while (getline(file, line)) {
        stringstream ss(line);
        Student student;
        string gradeStr;
        
        // Parse the line
        getline(ss, student.firstName, ',');
        getline(ss, student.lastName, ',');
        getline(ss, student.subject, ',');
        getline(ss, gradeStr, ',');
        student.grade = stoi(gradeStr);  // Convert grade to integer
        
        students.push_back(student);
    }

    return students;
}

int main() {
    vector<Student> students = readCSV("students.csv");

    // Print first 5 students
    for (int i = 0; i < 5; i++) {
        cout << students[i].firstName << " " << students[i].lastName << ", " 
             << students[i].subject << ", Grade: " << students[i].grade << endl;
    }

    return 0;
}