a, b = map(int, input().split())

result = 1
m = a * (a + 1) // 2

while b != 0:    
    result = (result * m) % a
    b >>= 1

print(result)