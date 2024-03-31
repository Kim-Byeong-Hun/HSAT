full_time = 0
for i in range(5):
    a, b = input().split()
    a_min = (int(a[0:2]) * 60) + (int(a[3:5]) * 1)
    b_min = (int(b[0:2]) * 60) + (int(b[3:5]) * 1)
    full_time += b_min-a_min

print(full_time)