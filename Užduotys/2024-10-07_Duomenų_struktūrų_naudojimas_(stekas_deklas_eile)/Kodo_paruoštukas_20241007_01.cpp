#include <iostream>
#include <queue>
#include <stack>
#include <deque>

class BankTransactions {
public:
    std::queue<std::string> queue;  // Naudojame kaip eilę
    std::stack<std::string> stack;  // Naudojame kaip steką
    std::deque<std::string> deq;    // Naudojame kaip deklą

    // Eilės funkcijos
    void enqueue_transaction(const std::string& transaction) {
        // TODO: įdėti elementą į eilę
        // queue.
    }

    std::string dequeue_transaction() {
        if (!queue.empty()) {
            // TODO: paimti pirmą elementą iš eilės
            // std::string front = queue.
            //
            return front;
        }
        return "Queue is empty";
    }

    // Steko funkcijos
    void push_transaction(const std::string& transaction) {
        // TODO: įdėti elementą į steką
        // stack.
    }

    std::string pop_transaction() {
        if (!stack.empty()) {
            // TODO: paimti paskutinį elementą iš steko 
            // std::string top = 
            // 
            return top;
        }
        return "Stack is empty";
    }

    // Deklo funkcijos
    void add_front_transaction(const std::string& transaction) {
        // TODO: įdėti elementą į priekį
        // deq.
    }

    void add_rear_transaction(const std::string& transaction) {
        // TODO: įdėti elementą į priekį
        // deq.
    }

    std::string remove_front_transaction() {
        if (!deq.empty()) {
            // TODO: paimti pirmą elementą iš deklo
            // std::string front = 
            //
            return front;
        }
        return "Deque is empty";
    }

    std::string remove_rear_transaction() {
        if (!deq.empty()) {
            // TODO: paimti paskutinį elementą iš deklo
            // std::string back = 
            // 
            return back;
        }
        return "Deque is empty";
    }
};

int main() {
    BankTransactions bt;

    // Eilės operacijos
    bt.enqueue_transaction("Client 1");
    bt.enqueue_transaction("Client 2");
    std::cout << "Eilėje aptarnaujamas: " << bt.dequeue_transaction() << std::endl;  // Client 1

    // Steko operacijos
    bt.push_transaction("Client 1");
    bt.push_transaction("Client 2");
    std::cout << "Steke aptarnaujamas: " << bt.pop_transaction() << std::endl;  // Client 2

    // Deklo operacijos
    bt.add_rear_transaction("Client 1");
    bt.add_front_transaction("VIP Client");
    std::cout << "Dekle aptarnaujamas iš priekio: " << bt.remove_front_transaction() << std::endl;  // VIP Client
    std::cout << "Dekle aptarnaujamas iš galo: " << bt.remove_rear_transaction() << std::endl;  // Client 1

    return 0;
}
