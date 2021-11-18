#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argument: ". format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument: ". format(len(sys.argv) - 1))
        for i, arg in range(1, len(sys.argv)):
            if i == 0:
                continue
            print('{}: {}'.format(len(sys.argv) - 1, arg))
    else:
        print("{} argument: ". format(len(sys.argv) - 1))
        for i, arg in range(1, len(sys.argv)):
            if i == 0:
                continue
            print('{}: {}'.format(i, arg))
