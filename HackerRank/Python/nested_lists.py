n = int(input())

students = []
scores = []
for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
    scores.append(grade)

scores = sorted(set(scores))

s = []
for i in students:
    if scores[1] == i[1]:
        s.append(i[0])

final = sorted(s)

i = 0
while i < len(final):
    print(final[i])
    i += 1
