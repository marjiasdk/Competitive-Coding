a = input()

found = False  #  i needed to use a boolean value
i = 0
while i < len(a) - 1:  #  - 1 so that a[i + 1] is in range
    if a[i] == "s":
        if a[i + 1] == "s":
            found = True
    i += 1

if found == True:
    print("hiss")
else:
    print("no hiss")