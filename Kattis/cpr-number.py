a = input()

b = int(a[0]) * 4
c = int(a[1]) * 3
d = int(a[2]) * 2
e = int(a[3]) * 7
f = int(a[4]) * 6
g = int(a[5]) * 5
h = int(a[7]) * 4
i = int(a[8]) * 3
j = int(a[9]) * 2
k = int(a[10]) * 1

total = b + c + d + e + f + g + h + i + j + k

if total % 11 == 0:
    print("1")
else:
    print("0")