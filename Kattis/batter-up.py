a = int(input())

b = map(int, input().split())

c = []
for i in b:  #  this is how you get the individual values in b
    if i >= 0:
        c.append(i)

print(sum(c) / len(c))