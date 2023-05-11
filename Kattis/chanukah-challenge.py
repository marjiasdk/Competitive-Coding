
a = int(input())
i = 0
while i < a:
    b, c = map(int, input().split())
    i += 1

    j = 1
    total = 0
    while j < c:
        total += (c - j)
        j += 1
    print(b, (c * 2) + total)