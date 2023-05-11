#!/usr/bin/env python3

import sys
a = int(sys.argv[1])

list = []
i = 2
while a > 1:
    if (a % i == 0):
        list.append(i)
        a //= i
    else:
        i += 1
print(max(list))
