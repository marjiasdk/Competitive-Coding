a = input()
b = a.split()

i = 1
while i < int(b[2]) + 1:
    if (i % int(b[0]) == 0) and (i % int(b[1]) == 0):
        print("FizzBuzz")
    elif i % int(b[0]) == 0:
        print("Fizz")
    elif i % int(b[1]) == 0:
        print("Buzz")
    else:
        print(i)
    i += 1