a = input()

word = int(len(a) / 3)

words = []
for i in range(0, int(len(a)), word):
    words.append(a[i:i + word])

#  count how many original words appear in the text
#  if it is 2, then print the first element in the list
if (words.count(words[0]) == 2):
    print(words[0])
#  else, print the 2nd element in the list
else:
    print(words[1])