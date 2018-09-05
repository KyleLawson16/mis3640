'''
Exercise 1
'''
import math

# 1.

radius = 5
volume = (4 / 3 * math.pi * (radius**3))

print(f'1. The volume of a sphere with radius {radius} is {round(volume, 2)} units cubed.')

# 2.

price = 24.95
discount = 0.4
copies = 60
cost = (price * discount) + 3 + (0.75 * (copies - 1))

print(f'2. The total wholesale cost of {copies} copies is ${round(cost, 2)}.')

# 3.

easy_pace = 8 + (15/60)
tempo = 7 + (12/60)
total_time = (easy_pace * 2) + (tempo * 3)
start_time_min = (6*60) + 52
end_time_min = start_time_min + total_time
end_time = '{hours}:{minutes}'.format(hours=(round(end_time_min // 60)), minutes=(round(end_time_min % 60)))

print(f'3. You will get home for breakfast at {end_time} am.')

# 4.

start = 82
end = 89
difference = end - start
percent_change = difference / start * 100

print('4. Your average grade rose by {:04.1f}%'.format(percent_change))
