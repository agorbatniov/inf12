#include <iostream>
#include <deque>

int main() {
    std::deque<int> d;

    // Pridedame elementus į galą ir į priekį
    d.push_back(10);    // Prideda į galą
    d.push_front(20);   // Prideda į priekį

    // Pašaliname elementus iš galo ir priekio
    d.pop_back();       // Pašalina iš galo
    d.pop_front();      // Pašalina iš priekio

    // Patikriname, ar deklas tuščias
    if (d.empty()) {
        std::cout << "Deklas yra tuščias." << std::endl;
    }

    return 0;
}