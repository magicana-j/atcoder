n = int(input())
s = input()
t = input()

similar_list = [["0", "o"], ["1", "l"]]

flag = [0 for i in range(n)]
for i in range(n):
    if s[i] == t[i]:
        flag[i] = 1
    else:
        if (s[i] in similar_list[0] and t[i] in similar_list[0]) or (
            s[i] in similar_list[1] and t[i] in similar_list[1]
        ):
            flag[i] = 1
        else:
            flag[i] = 0
print(flag)
ans = 1
for i in flag:
    ans *= i
if ans == 1:
    print("Yes")
else:
    print("No")
