import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')

n, a, b = map(int, f.readline().strip().split())
goukei = 0
for i in range(1, n+1):
    my_list = list(map(int, str(i)))
    sm = sum(my_list)
    if sm >= a and sm <= b:
        goukei += i
print(goukei)
