#!/usr/bin/python3
for x in range(90, 64, -1):
    if x % 2 != 0:
        print(chr(x), end="")
    else:
        print(chr(x + 32), end="")
