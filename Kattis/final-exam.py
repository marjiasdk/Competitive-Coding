n = int(input())

count = []
i = 0
while i < n:
    s = input()
    count.append(s)
    i += 1

final = len(count) - 1
score = 0
for i in range(final):
    if count[i] == count[i + 1]:
        score += 1
print(score)