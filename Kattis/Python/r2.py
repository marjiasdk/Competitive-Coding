a, b = map(int, input().split())

if a < b:
    print((b - a) + b)
if a > b:
    print(b - (a - b))
if a == b:
    print(a or b)