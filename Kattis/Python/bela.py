a = input()
b = a.split()

dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}

not_dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0

}

i = 0
total = 0
while i < (4 * int(b[0])):
    c = input()
    if c[1] == b[1]:
        total += dominant[c[0]]
    else:
        total += not_dominant[c[0]]
    i += 1
print(total)
