import math

a = int(input())

i = 0
total = 0
while i < a:
    b = map(float, input().split())
    c = math.prod(b)
    total += c
    i += 1
print(total)