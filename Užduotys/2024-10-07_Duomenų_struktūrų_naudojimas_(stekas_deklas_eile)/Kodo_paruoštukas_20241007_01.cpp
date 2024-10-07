#include <iostream>
#include <queue>
#include <stack>
#include <deque>
#include <string>  // For using std::string

// Using standard library types without std:: prefix
using namespace std;

class BankTransactions {
public:
    queue<string> transactionQueue;  // Naudojame kaip eilę
    stack<string> transactionStack;  // Naudojame kaip steką
    deque<string> transactionDeque;  // Naudojame kaip deklą

    // Eilės funkcijos
    void enqueue_transaction(const string& transaction) {
        // TODO: įdėti elementą į eilę
        // transactionQueue.
    }

    string dequeue_transaction() {
        if (!transactionQueue.empty()) {
            // TODO: paimti pirmą elementą iš eilės
            // string front =
            //
            return front;
        }
        return "Queue is empty";
    }

    // Steko funkcijos
    void push_transaction(const string& transaction) {
        // įdėti elementą į steką
        //transactionStack.
    }

    string pop_transaction() {
        if (!transactionStack.empty()) {
            // TODO: paimti pirmą elementą iš steko
            // string top = transactionStack.top();
            //
            return top;
        }
        return "Stack is empty";
    }

    // Deklo funkcijos
    void add_front_transaction(const string& transaction) {
        // TODO: įdėti elementą į dekla iš priekio
        // transactionDeque.
    }

    void add_rear_transaction(const string& transaction) {
        // TODO: įdėti elementą į dekla iš galo
        // transactionDeque.
    }

    string remove_front_transaction() {
        if (!transactionDeque.empty()) {
            // TODO: paimti pirmą elementą iš deklo
            // string front = 
            //
            return front;
        }
        return "Deque is empty";
    }

    string remove_rear_transaction() {
        if (!transactionDeque.empty()) {
            // TODO: paimti paskutinį elementą iš deklo
            // string back = 
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
    cout << "Eilėje aptarnaujamas: " << bt.dequeue_transaction() << endl;  // Client 1

    // Steko operacijos
    bt.push_transaction("Client 1");
    bt.push_transaction("Client 2");
    cout << "Steke aptarnaujamas: " << bt.pop_transaction() << endl;  // Client 2

    // Deklo operacijos
    bt.add_rear_transaction("Client 1");
    bt.add_front_transaction("VIP Client");
    cout << "Dekle aptarnaujamas iš priekio: " << bt.remove_front_transaction() << endl;  // VIP Client
    cout << "Dekle aptarnaujamas iš galo: " << bt.remove_rear_transaction() << endl;  // Client 1

    return 0;
}
