g, t, n = map(int, input().split())

weight = map(int, input().split())

print(int((g - t) * 0.9 - sum(weight)))