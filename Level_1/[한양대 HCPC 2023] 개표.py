import sys

T = int(input())

for i in range(T):
    inputs = int(input())
    x = ''
    for i in range(inputs//5):
        x += '++++ '
    for j in range(inputs%5):
        x += '|'
    print(x)