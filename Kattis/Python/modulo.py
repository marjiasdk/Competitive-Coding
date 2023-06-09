i = 0
n = []
while i < 10:
    b = int(input())
    modulo = b % 42
    n.append(modulo)
    i += 1
print(len(set(n)))