while True:
    try:
        a, b, c = map(int, input().split())
        result = '0.'
        for i in range(c):
            if a < b:
                # shift one decimal to the right
                a = a * 10
                # integer division to get the next decimal value
                n = a // b
                a = a - (n * b)
                result = result + str(n)
            else:
                a = a - b
                result += '1'
        print(result)
    except EOFError:
        break