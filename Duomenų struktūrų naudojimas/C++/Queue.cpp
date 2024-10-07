#include <iostream>
#include <queue>

int main() {
    std::queue<std::string> queue;

    // Pridedame elementus (enqueue)
    queue.push("Element 1");
    queue.push("Element 2");

    // Pašaliname elementą (dequeue)
    queue.pop();

    // Peržiūrime pirmą elementą
    std::cout << "Pirmas elementas: " << queue.front() << std::endl;

    return 0;
}