# The Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#                         1  2  3  4  5  6  7   8   9   10  11  12

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo = fibonacci(8)
print(fibo)