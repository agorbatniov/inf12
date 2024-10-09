#include <iostream>
using namespace std;

int main() {
    // Masyvo sukūrimas
    int skaiciai[5] = {1, 2, 3, 4, 5};

    // Elementų pasiekimas
    cout << "Pirmas elementas: " << skaiciai[0] << endl;

    // Elementų keitimas
    skaiciai[2] = 10;
    cout << "Pakeistas trečias elementas: " << skaiciai[2] << endl;

    // Masyvo perėjimas ciklu
    for(int i = 0; i < 5; i++) {
        cout << skaiciai[i] << " ";
    }

    return 0;
}
