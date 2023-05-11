a = input()
b = input()

list = []
for i in range(0, len(b), 3):
    c = int(b[i: i + 3])
    list.append(c)

for x in list:
    d = a[x - 1]
    print(d, end="")