n = int(input())

scores = list(map(int, input().split()))

scores.sort()

list = []
for x in scores:
    if x < max(scores):
        list.append(x)

print(max(list))
