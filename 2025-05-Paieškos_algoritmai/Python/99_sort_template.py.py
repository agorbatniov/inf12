import time

def search(arr, search_value):
    return -1

arr = [64, 34, 25, 12, 22, 11, 90, 15, 5, 6]
search_value = 15
start_time = time.time()
found_index = search(arr, search_value)
end_time = time.time()

if found_index == -1:
    print(f"Ieskomas elementas \"{search_value}\" nerastas.")

print(f"Ieskomo elemento \"{search_value}\" indeksas yra {found_index} ir reiksme lygi \"{arr[found_index]}\".")
print(f"Vykdymo laikas (search name): {end_time - start_time:.6f} sek.")