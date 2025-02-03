def find_max_min(numbers):
    if not numbers:  # Jei sąrašas tuščias, grąžiname None
        return None, None
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return max_num, min_num

def calculate_sum(max_num, min_num):
    return max_num - min_num

# Pagrindinė programa
numbers = [10, 4, 8, 2, 5]
max_num, min_num = find_max_min(numbers)

if max_num is not None and min_num is not None:
    print("Didžiausias skaičius:", max_num)
    print("Mažiausias skaičius:", min_num)
    print("Jų suma:", calculate_sum(max_num, min_num))
else:
    print("Sąrašas tuščias.")