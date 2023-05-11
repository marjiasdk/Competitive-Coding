#!/usr/bin/env python3

import sys
a = int(sys.argv[1])

i = 0
total = 0
while i < a:
    if (i % 3 == 0) or (i % 5 == 0):
        total += i
    i += 1
print(total)
