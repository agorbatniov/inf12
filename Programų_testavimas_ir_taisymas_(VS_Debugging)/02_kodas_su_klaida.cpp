#include <iostream>
using namespace std;

// Funkcija, kuri apskaičiuoja stačiakampio plotą
double calculate_area(double length, double width) {
    return length + width; 
}

// Funkcija, kuri apskaičiuoja stačiakampio perimetrą
double calculate_perimeter(double length, double width) {
    return 2 * (length + width);
}

int main() {
    double length = 5.0;
    double width = 3.0;

    double area = calculate_area(length, width);
    double perimeter = calculate_perimeter(length, width);

    cout << "Plotas: " << area << endl;
    cout << "Perimetras: " << perimeter << endl;

    return 0;
}



