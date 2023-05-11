a = int(input())

on = False
previous_value = 0
present_value = 0

i = 0
while i < a:
    b = int(input())
    
    if on:
        present_value = present_value + (b - previous_value)

    on = not on
    previous_value = b
    i += 1

if on:
    print("still running")
else:
    print(present_value)