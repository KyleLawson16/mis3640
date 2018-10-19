import os
# print(os.getcwd())

# fout = open('output.txt', 'w')
#
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
#
# line2 = "Before you call him a man?\n"
# fout.write(line2)
#
# fout.close()
#
# print(os.path.abspath('output.txt'))
# print (os.path.exists('output.txt'))
# print (os.path.exists('input.txt'))

import pickle

# t1 = [1, 2, 3]
#
# f = open('save.p', 'wb')
# s = pickle.dump(t1, f)
# f.close()

t2 = pickle.load(open('save.p', 'rb'))
print(t2)
