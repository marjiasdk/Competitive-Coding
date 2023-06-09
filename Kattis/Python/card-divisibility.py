a, b = map(int, input().split())

remainder = (b - a + 1) * (a + b) // 2 % 9
print(remainder)
