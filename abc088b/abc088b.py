import os
dirname = os.path.dirname(__file__)

in_file = dirname + '/input.txt'
f = open(in_file, 'r', encoding='UTF-8')

n = int(f.readline())
cards = list(map(int, f.readline().strip().split()))
cards = sorted(cards, reverse=True)
alice = 0
bob = 0
for i in range(0, n, 2):
    alice += cards[i]
if n % 2 == 1:
    for i in range(1, n-1, 2):
        bob += cards[i]
else:
    for i in range(1, n+1, 2):
        bob += cards[i]
print(alice - bob)
