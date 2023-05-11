while True:
    try:
        b = input()
        final = eval(b)
        ans = format(final, ".2f")
        print(ans)
    except EOFError:
        break