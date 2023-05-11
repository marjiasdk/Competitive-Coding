a = int(input())

i = 0
while i < a:
    b = input()
    c = b.split()
    d = (int(c[1]) - int(c[2]))
    if int(c[0]) < d:
        print("advertise")
    elif int(c[0]) == d:
        print("does not matter")
    else:
        print("do not advertise")
    i += 1