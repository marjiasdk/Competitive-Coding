a, b, c = sorted((map(int, input().split())))
letters = input()

result = []
for i in letters:
    if i == "A":
        result.append(a)
    elif i == "B":
        result.append(b)
    else:
        result.append(c)

non_list = " ".join(map(str, result))

print(non_list)