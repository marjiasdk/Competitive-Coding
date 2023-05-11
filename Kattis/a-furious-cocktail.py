n, s = map(int, input().split())

i = 0
lst = []
while i < n:
    b = int(input())
    lst.append(b)
    i += 1

lst.sort(reverse=True)

i = 0
while i < len(lst):
    if lst[i] - s * (n - i - 1) <= 0:
        print("NO")
        break
    i += 1
else:
    print("YES")
