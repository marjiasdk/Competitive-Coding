a = input()

i = 0
while a[i] != "(":

    j = 0
    while a[j] != ")":
        j += 1

    i += 1

if len(a[:i]) == len(a[j:]) - 1:
    print("correct")
else:
    print("fix")