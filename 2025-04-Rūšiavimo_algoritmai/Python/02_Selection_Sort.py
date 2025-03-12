import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]  
        arr[min_index] =temp


arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
start_time = time.time()
selection_sort(arr)
end_time = time.time()

print("Isrusiuotas masyvas:", arr)
print(f"Vykdymo laikas (Selection Sort): {end_time - start_time:.6f} sek.")