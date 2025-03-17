import csv

# Read CSV file and store it in a list
students_list = []

with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        students_list.append({
            "First Name": row[0],
            "Last Name": row[1],
            "Subject": row[2],
            "Grade": int(row[3])
        })

# Print first 5 rows of the list
for student in students_list[:5]:
    print(student)