# Exercise 3

# Split
sentence = 'Print this sentence one word at a time.'
split_words = sentence.split(' ')
for word in split_words:
    print(word)

# Strip
sentence = '       Remove all the spaces from this sentence.                  '
cleaned_sentence = sentence.strip()
print(cleaned_sentence)

# Replace
sentence = 'Capitalize kyle in this sentence.'
cleaned_sentence = sentence.replace('k', 'K')
print(cleaned_sentence)

# Exercise 4

items = [
    'bananas',
    'rice',
    'paprika',
    'potato chips'
]

# Part 1.

def print_receipt1(items):
    total_price = 0
    for item in items:
        price = 0
        for i in item:
            price += ord(i) - 96
        print(f'{item} ${price}')
        total_price += price
    print('-' * 20)
    print(f'Total ${total_price}')

print_receipt1(items)

# Part 2.

def print_receipt2(items):
    total_price = 0
    max_length = len(items[3]) + 10
    for item in items:
        price = 0
        for i in item:
            price += ord(i) - 96
        total_price += price
        price_string = '${0:.2f}'.format(price)
        num_of_spaces = max_length - len(item) - len(price_string)
        item_string = item + ' ' * num_of_spaces + price_string
        print(item_string)

    print('-' * max_length)
    total_price_string = '${0:.2f}'.format(total_price)
    num_of_spaces = max_length - len('Total') - len(total_price_string)
    print('Total' + ' ' * num_of_spaces + total_price_string)

print_receipt2(items)


# Part 3.

def print_receipt3(items):
    total_price = 0
    max_length = len(max(items, key=len)) + 10
    for item in items:
        price = 0
        for i in item:
            price += ord(i) - 96
        total_price += price
        price_string = '${0:.2f}'.format(price)
        num_of_spaces = max_length - len(item) - len(price_string)
        item_string = item + ' ' * num_of_spaces + price_string
        print(item_string)

    print('-' * max_length)
    total_price_string = '${0:.2f}'.format(total_price)
    num_of_spaces = max_length - len('Total') - len(total_price_string)
    print('Total' + ' ' * num_of_spaces + total_price_string)

print_receipt3(items)
