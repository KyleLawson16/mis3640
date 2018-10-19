import random

called_numbers = []

while len(called_numbers) < 5:
    number = random.randint(1,71)
    if number not in called_numbers:
        called_numbers.append(number)

mega_ball = random.randint(1,26)

print(f'The numbers are {called_numbers} and the mega ball is {mega_ball}')
