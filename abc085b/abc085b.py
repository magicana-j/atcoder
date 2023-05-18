import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')

n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
new_a = set(a)
print(len(new_a))
