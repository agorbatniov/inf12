from collections import deque

# Banko operacijų klasė
class BankTransactions:
    def __init__(self):
        self.queue = deque()  # Naudojame kaip eilę
        self.stack = deque()  # Naudojame kaip steką
        self.deque = deque()  # Naudojame kaip deklą
    
    # Eilės funkcijos
    def enqueue_transaction(self, transaction):
        # TODO: įdėti elementą į eilę
        # self.queue.
        print(f"[Elementas {transaction} įdėtas į eilę]")
    
    def dequeue_transaction(self):
        if self.queue:
            print("[Gauname elementą iš eilės]")
            # TODO: paimti pirmą elementą iš eilės
            # return self.queue
        return None
    
    # Steko funkcijos
    def push_transaction(self, transaction):
        # TODO: įdėti elementą į steką
        # self.stack.
        print(f"[Elementas {transaction} įdėtas į steką]")
    
    def pop_transaction(self):
        if self.stack:
            print("[Gauname elementą iš steko]")
            # TODO: paimti paskutinį elementą iš steko
            # return self.stack.
        return None
    
    # Deklo funkcijos
    def add_front_transaction(self, transaction):
        # TODO: įdėti elementą į priekį
        # self.deque.
        print(f"[Elementas {transaction} įdėtas į deklo galą]")
    
    def add_rear_transaction(self, transaction):
        # TODO: įdėti elementą į priekį
        # self.deque.
        print(f"[Elementas {transaction} įdėtas į deklo priekį]")
    
    def remove_front_transaction(self):
        if self.deque:
            print("[Gauname elementą iš deklo iš priekio]")
            # TODO: paimti pirmą elementą iš deklo
            # return self.deque.
        return None
    
    def remove_rear_transaction(self):
        if self.deque:
            print("[Gauname elementą iš deklo iš galo]")
            # TODO: paimti paskutinį elementą iš deklo
            # return self.deque.
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
