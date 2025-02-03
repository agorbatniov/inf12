def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade  
    average = total / len(grades)  
    return average

def is_passed(average):
    if average > 5:  
        return True
    else:
        return False

# Pagrindinė programa
grades = [8, 7, 6, 9, 4]  # Pavyzdiniai pažymiai
average = calculate_average(grades)
print("Vidurkis:", average)
print("Ar išlaikė egzaminą?", is_passed(average))