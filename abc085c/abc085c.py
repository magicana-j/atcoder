import time
import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input1.txt'
f = open(in_file, 'r', encoding='UTF-8')

start = time.time()

text = f.readlines()
n, y = map(int, text[0].strip().split())
# print(n, y)
flag = 0
answers = []
for i in range(y//10000+1):
    for j in range(y//5000+1):
        for k in range(y//1000+1):
            goukei = 10000*i + 5000*j + 1000*k
            if goukei == y and i+j+k == n:
                answers.append([i, j, k])
                flag = 1
        if flag==1:
            break
    if flag==1:
        break

if flag == 1:
    print(" ".join(map(str, answers[0])))
if flag == 0:
    print(-1, -1, -1)

end = time.time()-start
print(end,"秒")