n = int(input())
        
elements = input().split()
arr = [int(i) for i in elements]

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    # prcision is 6 decimal places
    print(f"{pos/total:.6f}")
    print(f"{neg/total:.6f}")
    print(f"{zero/total:.6f}")

plusMinus(arr)