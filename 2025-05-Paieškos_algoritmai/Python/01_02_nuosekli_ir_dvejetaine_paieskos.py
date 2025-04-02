import time

def sequential_search(data, target):
    """Nuosekli paieška."""
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

def binary_search(data, target):
    """Dvejetainė paieška (duomenys turi būti surūšiuoti)."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Pagrindinė programa

# Testuojamos reikšmės
targets = [90, 15, 66]
data1 = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]


for target in targets:
    data2 = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
    
    start = time.time()
    sequential_result = sequential_search(data1, target)
    sequential_time = time.time() - start
    
    start = time.time()
    data2.sort()  # Dvejetainė paieška veikia tik su surūšiuotais duomenimis
    binary_result = binary_search(data2, target)
    binary_time = time.time() - start
    
    print(f"Paieška: {target}")
    if sequential_result == -1:
        print(f"Nuosekli paieška: NERASTA, laikas {sequential_time:.6f} s")
    else:
        print(f"Nuosekli paieška: indeksas {sequential_result}, {target}=={data1[sequential_result]}, laikas {sequential_time:.6f} s")

    if binary_result == -1:
        print(f"Dvejetainė paieška: NERASTA, laikas {sequential_time:.6f} s")
    else:
        print(f"Dvejetainė paieška: indeksas {binary_result}, {target}=={data2[binary_result]}, laikas {binary_time:.6f} s")
    print("-" * 40)
