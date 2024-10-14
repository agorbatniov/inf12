def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Randame vidurį
        
        if arr[mid] == target:
            return mid  # Elementas rastas
        
        elif arr[mid] < target:
            left = mid + 1  # Ieškome dešinėje pusėje
        
        else:
            right = mid - 1  # Ieškome kairėje pusėje
    
    return -1  # Elementas nerastas

# Pavyzdys:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f'Elementas rastas indeksu {result}')
else:
    print('Elementas nerastas')
