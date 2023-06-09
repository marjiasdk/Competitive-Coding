import sys

for line in sys.stdin:
    num = int(line)
    counter = 2
    temp = 1
    while temp < num:
        if counter == 2:
            counter = 9
        else:
            counter = 2
        temp *= counter
    if counter == 2:
        print("Ollie wins.")
    else:
        print("Stan wins.")