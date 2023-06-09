n = int(input())

i = 0
win = 0
while i < n:
    command = input()
    if "CD" not in command:
        win += 1
    else:
        pass   
    i += 1

print(win)