N = int(input())

bin = bin(N)[2:]
count = bin.count('1')

print(2 ** count)