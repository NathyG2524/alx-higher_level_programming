#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print(f"{len(sys.argv)} arguments. ")
    elif len(sys.argv) == 1:
        print(f"{len(sys.argv)} argument: ")
        for i, arg in enumerate(sys.argv):
            print('{}: {}'.format(len(sys.argv), arg))
    else:
        print(f"{len(sys.argv)} arguments: ")
        for i, arg in enumerate(sys.argv):
            print('{}: {}'.format(i, arg))
