def add(a, b):
    return a + b  # Correct implementation

def subtract(a, b):
    return a - b  # Correct implementation

def multiply(a, b):
    return a * b  # Correct implementation

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"  # Logical flaw: should raise an exception
    return a / b

def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        return "Error: Invalid operation"  # Logical flaw: no exception for invalid operation

print("Welcome to the Calculator App!")
print("Available operations: add, subtract, multiply, divide")

a = input("Enter first number: ")  # Flaw: no input validation
b = input("Enter second number: ")  # Flaw: no input validation
operation = input("Enter operation: ")

result = calculate(operation, a, b)  # Flaw: input values are strings, not numbers
print(f"The result is: {result}")
