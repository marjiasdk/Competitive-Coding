a = int(input())
while a != -1:

    total = 0
    prev = 0
    for i in range(a):
        miles, hours = map(int, input().split())
        total += (hours - prev) * miles
        prev = hours
    print(total, "miles")

    a = int(input())