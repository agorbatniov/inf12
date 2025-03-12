import random

def generate_random_numbers():
    arr = [random.randint(1, 1000000) for _ in range(1000)]
    return arr

# Generuojame atsitiktinius skaièius
arr = generate_random_numbers()
print(arr)