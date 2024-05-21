import sys

N = int(input())

text = ''
a = []
for i in range(N):
    a.append(list(input().upper().split()))

for i in a:
    text += i[1][i[0].find('X')]
    
print(text)