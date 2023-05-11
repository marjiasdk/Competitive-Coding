n = int(input())
price = list(map(int, input().split()))
price.sort(reverse=True)

i = 2
discount = 0
while i < len(price):
    discount += price[i]
    i += 3
print(discount)