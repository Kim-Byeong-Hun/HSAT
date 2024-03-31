import sys

n = int(input())
locate = list(map(int, input().split()))

a = locate[0]
b = []
for i in locate:
    if i != a:
        b.append(i - a)
        a = i

print(b.count(min(b)))


