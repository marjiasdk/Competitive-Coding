a, b, h = map(int, input().split())

distance = 0
count = 0
while distance < h:
    distance += a
    count += 1

    if distance >= h:
        break
    distance -= b
print(count)