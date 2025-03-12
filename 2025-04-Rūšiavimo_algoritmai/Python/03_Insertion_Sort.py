import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
start_time = time.time()
insertion_sort(arr)
end_time = time.time()

print("Isrusiuotas masyvas:", arr)
print(f"Vykdymo laikas (Insertion Sort): {end_time - start_time:.6f} sek.")