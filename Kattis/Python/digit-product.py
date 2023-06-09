n = input()

i = 1
while i < len(n):
    product = 1
    for digit in n:
        if digit != "0":
            product *= int(digit)
    n = str(product)
print(n)