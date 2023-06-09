n = float(input())

miles = n * (5280 / 4854)

s = round(miles, 3)

print(int(s * 1000))