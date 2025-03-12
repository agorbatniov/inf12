import time

def sort(arr):
    pass


arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
start_time = time.time()
sort(arr)
end_time = time.time()

print("Isrusiuotas masyvas:", arr)
print(f"Vykdymo laikas (Sort name): {end_time - start_time:.6f} sek.")