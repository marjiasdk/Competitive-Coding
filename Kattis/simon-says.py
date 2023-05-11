n = int(input())

i = 0
while i < n:
    string = input() 
    if "Simon says" in string[0:11]:
        print(string[11:])
    i += 1