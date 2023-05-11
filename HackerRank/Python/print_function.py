n = int(input())

i = 1
list = []
while i < n:
    list.append(i)
    i += 1
list.append(n)

string = "".join(map(str, list))
print(string)
