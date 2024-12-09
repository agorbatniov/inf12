// calculator.cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Funkcijos
double add(double a, double b) {
    return a + b; // Teisinga įgyvendinimas
}

double subtract(double a, double b) {
    return a - b; // Teisinga įgyvendinimas
}

double multiply(double a, double b) {
    return a * b; // Teisinga įgyvendinimas
}

double divide(double a, double b) {
    if (b == 0) {
        return -1; // Klaida: reikėtų mesti išimtį
    }
    return a / b;
}

double calculate(const string& operation, double a, double b) {
    if (operation == "add") {
        return add(a, b);
    } else if (operation == "subtract") {
        return subtract(a, b);
    } else if (operation == "multiply") {
        return multiply(a, b);
    } else if (operation == "divide") {
        return divide(a, b);
    } else {
        return -1; // Klaida: reikėtų mesti išimtį
    }
}

// Pagrindinė programa (su tyčinėmis klaidomis)
int main() {
    cout << "Welcome to the Calculator App!" << endl;
    cout << "Available operations: add, subtract, multiply, divide" << endl;

    string operation;
    double a, b;

    cout << "Enter first number: "; // Nėra įvesties validacijos
    cin >> a;
    cout << "Enter second number: "; // Nėra įvesties validacijos
    cin >> b;
    cout << "Enter operation: ";
    cin >> operation;

    double result = calculate(operation, a, b); // Nėra tinkamos klaidų validacijos

    if (result == -1) {
        cout << "Error: Invalid operation or division by zero." << endl;
    } else {
        cout << "The result is: " << result << endl;
    }

    return 0;
}
