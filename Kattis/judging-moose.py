left, right = map(int, input().split())

if left == right == 0:
    print("Not a moose")
elif left == right:
    total = str(left + right)
    print("Even " + total)
elif left > right:
    total = str(2 * left)
    print("Odd " + total)
else:
    total = str(2 * right)
    print("Odd " + total)