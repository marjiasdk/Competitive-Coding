# cook your dish here

n = int(input())

i = 0
while i < n:
    a, b = map(int, input().split())
    if a + b > 6:
        print("YES")
    else:
        print("NO")
    i += 1