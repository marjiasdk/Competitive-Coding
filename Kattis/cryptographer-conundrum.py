a = input()

i = 0
list = []
while i < len(a):
    list.append(a[i])
    i += 1

i = 0
total = 0
while i < len(list):
    #  if a letter in the string is not equal to a letter in "PER", you add the days needed to turn it into "PER"
    if list[i] != "PER"[i % 3]:
        total += 1
    i += 1
print(total)