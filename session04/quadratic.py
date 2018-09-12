import math

def quadratic(a, b, c):
    answer1 = (-b + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    answer2 = (-b - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    return answer1, answer2

answer1, answer2 = quadratic(2, -1, -1)
print(f'x = {answer1} and x = {answer2}')
