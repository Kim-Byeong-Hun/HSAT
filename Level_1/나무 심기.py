import sys

n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(0, len(a)):
    x = a[i]
    for j in range(i+1, len(a)):
        b.append(x * a[j])

print(max(b))