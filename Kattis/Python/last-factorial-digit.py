import math

a = int(input())

i = 0
while i < a:
    n = int(input())
    c = math.factorial(n)
    d = str(math.factorial(n))
    print(d[len(d) - 1])
    i += 1