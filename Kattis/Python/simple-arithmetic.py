from decimal import Decimal

value = input().split()

a = Decimal(value[0])
b = Decimal(value[1])
c = Decimal(value[2])

answer = a * b / c

print(Decimal(answer))