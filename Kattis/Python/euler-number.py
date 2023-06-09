import math

n = int(input())

e = n + 1

ans = 0
i = 0
for i in range(e):
    if n < 17:
        ans += 1/math.factorial(i)
    else:
        ans = 2.7182818284590455
print(ans)