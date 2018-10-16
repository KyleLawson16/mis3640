import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
               'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0 }

def select_student(class_roster):
    min_value = min(class_roster.values())
    pool = []
    for student in class_roster:
        if class_roster[student] == min_value:
            pool.append(student)

    chosen_one = pool[random.randint(0, len(pool))]
    class_roster[chosen_one] += 1
    return chosen_one


print(select_student(class_roster))
print(class_roster)
