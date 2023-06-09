import math

a = input()
b = a.split()

s = (int(b[0]) + int(b[1]) + int(b[2]) + int(b[3])) / 2 
e = math.sqrt((s - int(b[0])) * (s - int(b[1])) * (s - int(b[2])) * (s - int(b[3])))

print(e)