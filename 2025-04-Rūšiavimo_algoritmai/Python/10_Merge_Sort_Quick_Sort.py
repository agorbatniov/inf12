# Merge Sort algoritmas
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort algoritmas
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Testavimas
arr = [38, 27, 43, 3, 9, 82, 10]
print("Originalus masyvas:", arr)
print("Surikiuotas su Merge Sort:", merge_sort(arr))
print("Surikiuotas su Quick Sort:", quick_sort(arr))
