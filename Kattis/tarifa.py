a = int(input())
b = int(input())

i = 0
total = 0
while i < b:
    c = int(input())
    d = a - c
    total += d
    i += 1
print(total + a)