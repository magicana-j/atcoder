# n, m = map(int, input().split())

# a = []
# for i in range(m):
#     a.append(list(map(int, input().split())))

n = 4
m = 2
a = [[1, 2, 3, 4], [4, 3, 2, 1]]
print(a)

distance = []

for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(m):
            neighbor = 1
            if abs(a[m].index(i + 1) - a[m].index(j + 1)) == 1:
                neighbor *= 1
            else:
                neighbor = 0
        distance.append(i, j, neighbor)

print(distance)
