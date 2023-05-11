#!/usr/bin/env python3

import sys
a = int(sys.argv[1])

i = 0
b = 0
c = 1
total = 0
while i < a:
    b = b + c
    c = b - c
    if (c % 2 == 0) and c < a:
        total += c
    i += 1
print(total)
