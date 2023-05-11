import math

a = float(input())
b = float(input())

i = 0
total = 0
while i < b:
    c = map(float, input().split())
    d = math.prod(c)
    total += d
    i += 1

print(total * a)