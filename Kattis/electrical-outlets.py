a = int(input())

i = 0
while i < a:
    b = list(map(int, input().split()))

    j = 1
    total = 0
    while j < len(b):
        total += int(b[j])
        j += 1
    print(total - int(b[0]) + 1)
    i += 1