cuts = int(input())

r = 1 + int(cuts / 2)
c = 1 + (cuts - (r - 1))

print(c * r)