for x in range(int(input())):
    cities = [input() for x in range(int(input()))]
    number = set(cities)
    #  set only records elements ONCE
    print(len(number))