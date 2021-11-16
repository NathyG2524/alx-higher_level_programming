#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            upper = chr((ord(x)-97)+65)
        else:
            upper = x
        print(upper, end="")
    print('')
