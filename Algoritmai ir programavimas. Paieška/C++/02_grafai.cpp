#include <iostream>
#include <vector>
#include <tuple>

int main() {
    // Viršūnių sąrašas (vertices)
    std::vector<char> vertices = {'A', 'B', 'C', 'D', 'E'};
    
    // Briaunų sąrašas su svoriais (edges), naudojant std::tuple
    std::vector<std::tuple<char, char, int>> edges = {
        {'A', 'B', 4},
        {'A', 'C', 2},
        {'B', 'C', 5},
        {'B', 'D', 10},
        {'C', 'E', 3},
        {'D', 'E', 1}
    };

    // Spausdiname viršūnių sąrašą
    std::cout << "Viršūnių sąrašas: ";
    for (char v : vertices) {
        std::cout << v << " ";
    }
    std::cout << std::endl;

    // Spausdiname briaunų sąrašą su svoriais
    std::cout << "Briaunų sąrašas (pradinis taškas, galutinis taškas, svoris):" << std::endl;
    for (auto edge : edges) {
        std::cout << std::get<0>(edge) << " -> " << std::get<1>(edge) << " (svoris: " << std::get<2>(edge) << ")" << std::endl;
    }

    return 0;
}
