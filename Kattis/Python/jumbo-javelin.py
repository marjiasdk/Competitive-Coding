a = int(input())

i = 0
total = 0
while i < a:
    b = int(input())
    total += b
    i += 1
print(total - (i - 1))