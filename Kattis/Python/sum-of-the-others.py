import sys

for line in sys.stdin:
    numbers = list(map(int, line.split()))
    total = sum(numbers)
    for n in (numbers):
        if total - n == n:
            print(n)
            break