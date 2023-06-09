n = int(input())

i = 0
while i < n:
    string = input() 
    if "simon says" in string[0:11]:
        print(string[11:])
    else:
        print(" ")
    i += 1