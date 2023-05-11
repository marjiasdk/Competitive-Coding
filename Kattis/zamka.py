l = int(input())
d = int(input())
x = int(input())

result = []

for i in range(l, d + 1):

  sum = 0
  for j in range(len(str(i))):
    sum += int(str(i)[j])

  if sum == x:
    result.append(i)

print(min(result))
print(max(result))