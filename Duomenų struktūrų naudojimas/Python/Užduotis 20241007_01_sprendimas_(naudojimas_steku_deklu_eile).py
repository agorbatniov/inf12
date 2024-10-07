from collections import deque

# Banko operacijų klasė
class BankTransactions:
    def __init__(self):
        self.queue = deque()  # Naudojame kaip eilę
        self.stack = deque()  # Naudojame kaip steką
        self.deque = deque()  # Naudojame kaip deklą
    
    # Eilės funkcijos
    def enqueue_transaction(self, transaction):
        self.queue.append(transaction)
        print(f"[Elementas {transaction} įdėti į eilę]")
    
    def dequeue_transaction(self):
        if self.queue:
            print("[Gauname elementą iš eilės]")
            return self.queue.popleft()
        return None
    
    # Steko funkcijos
    def push_transaction(self, transaction):
        self.stack.append(transaction)
    
    def pop_transaction(self):
        if self.stack:
            return self.stack.pop()
        return None
    
    # Deklo funkcijos
    def add_front_transaction(self, transaction):
        self.deque.appendleft(transaction)
    
    def add_rear_transaction(self, transaction):
        self.deque.append(transaction)
    
    def remove_front_transaction(self):
        if self.deque:
            return self.deque.popleft()
        return None
    
    def remove_rear_transaction(self):
        if self.deque:
            return self.deque.pop()
        return None

# Pavyzdys
bt = BankTransactions()

# Eilės operacijos
bt.enqueue_transaction("Client 1")
bt.enqueue_transaction("Client 2")
print("Eilėje aptarnaujamas:", bt.dequeue_transaction())  # Client 1

# Steko operacijos
bt.push_transaction("Client 1")
bt.push_transaction("Client 2")
print("Steke aptarnaujamas:", bt.pop_transaction())  # Client 2

# Deklo operacijos
bt.add_rear_transaction("Client 1")
bt.add_front_transaction("VIP Client")
print("Dekle aptarnaujamas iš priekio:", bt.remove_front_transaction())  # VIP Client
print("Dekle aptarnaujamas iš galo:", bt.remove_rear_transaction())  # Client 1
