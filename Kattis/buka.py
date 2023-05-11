i = 0
list = []
while i < 3:
    n = input()
    list.append(n)
    i += 1

if list[1] == "*":
    print(int(list[0]) * int(list[2]))
else:
    print(int(list[0]) + int(list[2]))