n = int(input())

i = 0
list = []
while i < n:
    a = int(input())
    list.append(a)
    i += 1

while 0 < len(list):
    print(list.pop())