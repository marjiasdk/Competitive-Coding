m, a, b, c = map(int, input().split())

if m * 2 < a + b + c:
    print("impossible")
else:
    print("possible")