#include <iostream>
#include <stack>

int main() {
    std::stack<int> stack;

    // Pridedame elementus į steką
    stack.push(10);
    stack.push(20);

    // Pašaliname elementus iš steko
    stack.pop();    // Pašalina paskutinį elementą (20)
    stack.pop();    // Pašalina paskutinį elementą (10)

    // Patikriname, ar stekas tuščias
    if (stack.empty()) {
        std::cout << "Stekas yra tuščias" << std::endl;
    }

    return 0;
}
