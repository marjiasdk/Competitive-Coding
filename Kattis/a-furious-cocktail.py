n, s = map(int, input().split())

i = 0
list = []
while i < n:
    b = int(input())
    list.append(b)
    i += 1

list.sort(reverse=True)

i = 0
while i < len(list):
    if list[i] - s * (n - i - 1) <= 0:
        print("NO")
        break
    i += 1
else:
    print("YES")