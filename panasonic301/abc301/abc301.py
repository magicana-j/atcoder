import os
from itertools import chain
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')


def print_list(my_list):
    print(" ".join(map(str, my_list)))


def serial(a, b):
    if b - a > 1:
        result = []
        for i in range(a+1, b, 1):
            result.append(i)
    elif a - b > 1:
        result = []
        for i in range(a-1, b, -1):
            result.append(i)
    else:
        result = [a]
    print(result)
    return result


def ins_list(l1):
    leng = len(l1)
    temp = []
    for i in range(leng-1):
        temp.append(serial(l1[i], l1[i+1]))
    result = temp.append(l1[-1])
    return result


n = int(f.readline())
a = list(map(int, f.readline().split()))

print(a)
print(ins_list(a))
