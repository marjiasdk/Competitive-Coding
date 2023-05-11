a, b = map(int, input().split())

ways = [0] * (a + b + 1)

i = 1
while i <= a:

  j = 1
  while j <= b:
    ways[i + j] += 1
    j += 1

  i += 1

i = 0
while i < len(ways):
    if a > b:
        if ways[i] == b:
            print(i)
    elif a < b:
        if ways[i] == a:
            print(i)
    elif a == b:
        if ways[i] == a:
            print(i)
    i += 1