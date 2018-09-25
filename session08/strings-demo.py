team = 'New England Patriots'
letter = team[1]

split_team = team.split(' ')
for i in split_team:
    print(i)

def find(word, letter):
    index = 0
    for i, val in enumerate(word):
        if word[i] == letter:
            return i
        i += 1
    return -1

print(find(team, 'E'))


def count(s, letter):
    amt = 0
    for i in s:
        if i == letter:
            amt += 1
    return amt

print(count(team, 'a'))

new_team = team.upper()
print(new_team)
