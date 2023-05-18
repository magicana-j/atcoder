import time
import os

dirname = os.path.dirname(__file__)

in_file = dirname + "/input1.txt"
f = open(in_file, "r", encoding="UTF-8")

start = time.time()

text = f.readlines()
n, y = map(int, text[0].strip().split())
# print(n, y)
flag = 0
for i in range(n + 1):
    if flag == 1:
        break
    for j in range(n - i + 1):
        k = (y - 10000 * i - 5000 * j) // 1000
        if k >= 0 and i + j + k == n:
            print(i, j, k)
            flag = 1
            break

if flag == 0:
    print(-1, -1, -1)

end = time.time() - start
print(end, "秒")
