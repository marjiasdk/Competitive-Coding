a = input()
b = a.split()

n = int(b[0])
p = int(b[1])
s = int(b[2])

j = 0
while j < s:
    c = input()
    d = c.split()
    j += 1

    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1

    contains = False
    for x in d[1:]:
        if x == p:
            contains = True

    if contains:
        print("KEEP")
    else:
        print("REMOVE")