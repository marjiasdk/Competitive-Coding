a = input()
b = a.split()
d = int(b[0]) - int(b[1])
e = int(b[0])

i = 0
total = 0
while i < int(b[1]):
    c = int(input())
    total += c
    i += 1

f = total + (d * -3)
g = total + (d * 3)

print(f / e)
print(g / e)