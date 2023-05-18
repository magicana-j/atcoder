import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def print_list(my_list):
    print(" ".join(map(str, my_list)))


n = int(f.readline())
a = list(f.readline().strip())
# print(n)
# print(a)

t_s = a.count('T')
a_s = a.count('A')

if t_s > a_s:
    print('T')
elif t_s < a_s:
    print('A')
else:
    if a[-1] == 'T':
        print('A')
    else:
        print('T')
