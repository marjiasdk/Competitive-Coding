a = input()

#  set() prints out all elements and doesn't have duplicates

if len(a) != len(set(a)):
    print("0")
else:
    print("1")