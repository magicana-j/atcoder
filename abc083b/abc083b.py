import os

dirname = os.path.dirname(__file__)

fname = "input.txt"
in_file = dirname + "/" + fname
f = open(in_file, "r", encoding="UTF-8")


def solve(n: int, a: int, b: int):
    goukei = 0
    for i in range(1, n + 1):
        my_list = list(map(int, str(i)))
        sm = sum(my_list)
        if sm >= a and sm <= b:
            goukei += i
    return goukei


n, a, b = map(int, f.readline().strip().split())
print(solve(n, a, b))
