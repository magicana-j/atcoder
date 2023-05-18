import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input1.txt'
f = open(in_file, 'r', encoding='UTF-8')

text = f.readlines()
n, y = map(int, text[0].strip().split())
print(n, y)
