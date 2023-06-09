i = 0
list = []
while i < 5:
    a = map(int, input().split())
    b = sum(a)
    list.append(b)
    i += 1

index = list.index(max(list))
print(int(index) + 1, max(list))