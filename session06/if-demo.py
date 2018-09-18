# age = input('please enter your age: ')
#
# if int(age) >= 18:
#     print('adult')
# elif int(age) >= 6:
#     print('teenager')
# else:
#     print('kid')


# BMI calculator

system = input('What system are you using (M for metric, US for customary): ')
weight = int(input('What is your weight: '))
height = int(input('What is your height: '))

def bmi_calculator(system, weight, height):
    bmi = (weight / (height ** 2))
    if system == 'US':
        bmi = bmi * 703
    if bmi < 18.5:
        return bmi, 'underweight'
    elif 18.5 <= bmi < 25:
        return bmi, 'normal weight'
    elif 25 <= bmi < 30:
        return bmi, 'overweight'
    else:
        return bmi, 'obese'

bmi, status = bmi_calculator(system, weight, height)
print(f'Your bmi is {bmi} and you are {status}.')


def compare(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return 'string involved'
    else:
        if a > b:
            return 'bigger'
        elif a == b:
            return 'equal'
        else:
            return 'smaller'

a = 'hello'
b = 3
c = 5

print(compare(a, b))
print(compare(b, c))


def cigar_party(cigars, is_weekend):
  return is_weekend and cigars >= 40 or 40 <= cigars <= 60
