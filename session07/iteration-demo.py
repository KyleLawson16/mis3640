import time

def sum_int(range):
    sum = 0
    for i in range:
        sum += i
    return sum

# print(sum_int(range(1, 1001)))

def factorial(range):
    result = 1
    for i in range:
        result *= i
    return result


# print(factorial(range(1, 11)))


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print('Blastoff!')

# countdown(5)
