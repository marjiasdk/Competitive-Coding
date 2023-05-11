result = 1
n = int(input())

for i in range(1, n + 1):

    result *= i

    while result % 10 == 0:
        result //= 10
    
    result %= 1000000000000

print(str(result)[-3:])