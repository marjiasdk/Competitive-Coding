a = int(input())

b = input()
c = b.split()

i = 0
total = 0
while i < len(c):
    if int(c[i]) < 0:
        total += 1
    i += 1
print(total)