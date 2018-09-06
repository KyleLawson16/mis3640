'''
Age Validator w/ Error Handling
'''

age = input('Please enter your age: ')

def check_age(age):
    try:
        age = int(age)
        if age >= 21:
            print('yes, you can.')
        else:
            print('sorry, you cannot.')

    except:
        age = input('Please enter a valid number: ')
        check_age(age)

check_age(age)
