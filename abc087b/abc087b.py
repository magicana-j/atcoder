# coding: utf-8

a = 2
b = 2
c = 2
x = 100

cnt = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*(i) + 100*(j) + 50*(k) == x:
                cnt += 1
print(cnt)
