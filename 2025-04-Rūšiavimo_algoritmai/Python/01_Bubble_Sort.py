import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]  
                arr[j + 1] =temp
                swapped = True

        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
start_time = time.time()
bubble_sort(arr)
end_time = time.time()

print("Isrusiuotas masyvas:", arr)
print(f"Vykdymo laikas (Bubble Sort): {end_time - start_time:.6f} sek.")