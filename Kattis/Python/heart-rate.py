a = int(input())

i = 0
while i < a:
    b = input()
    c = b.split()
    part1 = 60 * int(c[0])
    part2 = int(c[0]) * float(c[1])
    part3 = part1 / part2
    d = int(c[0]) * part3
    e = d - part3
    g = int(c[0]) * part3
    f = d + part3
    print(e)
    print(g)
    print(f)
    i += 1