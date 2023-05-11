a = int(input())

i = 0
total = 0
while i < a:
    b = int(input())
    c = str(b)
    d = c[len(c) - 1]
    e = c[:len(c) - 1]
    f = int(e) ** int(d)
    total += f
    i += 1
print(total)