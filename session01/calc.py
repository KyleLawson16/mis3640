'''
EXERCISE 1
'''

# 1. syntax error if you leave out the first or both. If you leave out the last, the print statement continues to the next line

# 2. syntax error if you leave out the first or both. If you leave out the last, the print statement continues to the next line

# 3. it's like doing 0 + 4, just returns 4

# 4. syntax error

# 5. syntax error

'''
EXERCISE 2

Run code in file for answers
'''

km = 10
min = 42
sec = 42

# 1.

def min_to_sec(min, sec):
    return (min * 60) + sec

print('1. There are %s seconds in %s minutes and %s seconds' %(min_to_sec(min, sec), min, sec))


# 2.

def km_to_mi(km):
    return round(km / 1.61, 2)

print('2. There are %s miles in %s kilometers' %(km_to_mi(km), km))


# 3.

def sec_to_min(sec):
    minutes = round(sec // 60)
    remainder = round(sec % 60)
    if minutes == 0:
        return '%s seconds' %(remainder)
    else:
        return '%s minutes %s seconds' %(minutes, remainder)

def min_per_mile(min, sec, km):
    total_sec = min_to_sec(min, sec)
    total_miles = km_to_mi(km)
    sec_per_mile = total_sec / total_miles
    return sec_to_min(sec_per_mile)

def miles_per_hour(min, sec, km):
    total_sec = min_to_sec(min, sec)
    hours = (total_sec / (60^2))
    total_miles = km_to_mi(km)
    miles_per_hour = round(total_miles / hours, 2)
    return '%s miles per hour' %(miles_per_hour)


print(
    '3. If you run a %s kilometer race in %s minutes %s seconds, your average pace is %s per mile and your average speed is %s.'
    %(km, min, sec, min_per_mile(min, sec, km), miles_per_hour(min, sec, km))
)
