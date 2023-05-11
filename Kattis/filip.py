a = input()
b = a.split()

if int(b[0][::-1]) > int(b[1][::-1]):
    print(b[0][::-1])
else:
    print(b[1][::-1])
