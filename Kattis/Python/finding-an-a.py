a = input()

i = 0
while i < len(a) and a[i] != "a":
    i += 1

print(a[i:])