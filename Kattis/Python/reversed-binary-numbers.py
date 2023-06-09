import math

a = int(input())
binary = bin(a)

need = bin(a)[2:]
final = need[::-1]
print(int(final, 2))