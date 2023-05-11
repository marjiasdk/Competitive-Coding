n = list(map(int, input().split()))

while n[0] is not 0:
    mixedfraction = []
    mixedfraction.append(n[0] // n[1])
    mixedfraction.append(n[0] % n[1])

    print(str(mixedfraction[0]), str(mixedfraction[1]), " / ", str(n[1]))
    n = list(map(int, input().split()))