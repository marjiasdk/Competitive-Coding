import math

a = input()
b = a.split()

d = math.sqrt(int(b[1]) ** 2 + int(b[2]) ** 2 + 0.01)

i = 0
while i < int(b[0]):
    c = int(input())
    if c < d:
        print("DA")
    else:
        print("NE")
    i += 1