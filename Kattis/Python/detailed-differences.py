number = int(input())

i = 0
while i < number:
  a = input()
  b = input()

  j = 0
  differences = ""
  while j < len(a) and len(b):
    if a[j] == b[j]:
      differences += "."
    if a[j] != b[j]:
      differences += "*"
    
    j += 1

  print(a)
  print(b)
  print(differences)
  i += 1