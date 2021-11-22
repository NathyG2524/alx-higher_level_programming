#!/usr/bin/python3
def multiple_returns(sentence):
    a = list(sentence)
    if len(a) == 0:
        a[0] = None
    return len(a), a[0]
