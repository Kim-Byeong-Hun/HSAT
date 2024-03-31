a, b, d = map(int, input().split())
time = 0

front = a * (d // a)
if d % a != 0:
    front_h = b * (d // a)
else:
    front_h = 0
time += front + front_h
time += d - front # touch

back = b * (d // b)

if d % b != 0:
    back_h = a * (d // b)
else:
    back_h = 0
time += back + back_h
time += d - back # touch

print(time)
