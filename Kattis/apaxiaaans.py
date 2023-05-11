word = input()

i = 0
compact = []
while i < len(word):
    compact.append(word[i])
    i += 1

i = 0
new = []
while i + 1 < len(compact):
    if compact[i] != compact[i + 1]:
        new.append(compact[i])
    i += 1

new.append(compact[-1])

answer = "".join(new)
print(answer)