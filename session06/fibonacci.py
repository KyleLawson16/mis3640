# 1, 1, 2, 3, 5, 8 . . .

def fibonacci(n):
    if n < 1:
        return 'invalid'
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
