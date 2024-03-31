import sys

N = int(input())

a = []

for i in range(N):
    a.append(list(map(int, input().split())))

b = []
for i in a:
    b.append(i[1])

print(a[b.index(min(b))][0], a[b.index(min(b))][1])