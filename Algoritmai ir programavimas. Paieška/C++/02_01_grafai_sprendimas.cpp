#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>

using namespace std;

void dijkstra(const unordered_map<char, unordered_map<char, int>>& graph, char start) {
    unordered_map<char, int> distances;
    for (const auto& vertex : graph) {
        distances[vertex.first] = numeric_limits<int>::max(); // Begalybė
    }
    distances[start] = 0;

    // Prioritetų eilė
    priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> priority_queue;
    priority_queue.push({0, start});

    while (!priority_queue.empty()) {
        auto [current_distance, current_vertex] = priority_queue.top();
        priority_queue.pop();

        // Tikriname, ar atstumas yra didesnis nei jau žinomas
        if (current_distance > distances[current_vertex]) {
            continue;
        }

        // Patikriname kaimyninius vertexus
        for (const auto& [neighbor, weight] : graph.at(current_vertex)) {
            int distance = current_distance + weight;

            // Atinaujiname atstumą, jei randame trumpesnį
            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                priority_queue.push({distance, neighbor});
            }
        }
    }

    // Išvedame trumpiausius atstumus
    cout << "Trumpiausi keliai nuo " << start << ":" << endl;
    for (const auto& [vertex, distance] : distances) {
        cout << vertex << ": " << distance << endl;
    }
}

int main() {
    // Pavyzdinis grafas (kaimynų sąrašas su svoriais)
    unordered_map<char, unordered_map<char, int>> graph = {
        {'A', {{'B', 4}, {'C', 2}}},
        {'B', {{'C', 5}, {'D', 10}}},
        {'C', {{'E', 3}}},
        {'D', {{'E', 1}}},
        {'E', {}}
    };

    // Iškviečiame Dijkstra's algoritmą
    char start_vertex = 'A';
    dijkstra(graph, start_vertex);

    return 0;
}
