fin = open('words.txt')
line = repr(fin.readline())
#https://docs.python.org/3/library/functions.html#repr

line = fin.readline()
word = line.strip()


def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

def is_abecedarian_while(word):
    i = 0
    while i < len(word):
        if word[i] < word[i+1]:
            return False
        i += 1
    return True

# print(is_abecedarian(word))
# print(is_abecedarian_recursive(word))
# print(is_abecedarian_while(word))

def has_three_consecutive(word):
    for i in word:
        print(word)

fin = open('words.txt')

def has_three_consecutive(fin):
    for line in fin:
        consecutive = 0
        word = line.strip()
        for index, letter in enumerate(word):
            if letter == word[index - 1]:
                consecutive += 1
        if consecutive == 3:
            return word

print(has_three_consecutive(fin))
