a = input()

i = 0
total = 0
while i < len(a):
    if a[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        total += 1
    i += 1
print(total)