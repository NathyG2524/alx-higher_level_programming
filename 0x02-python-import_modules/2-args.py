#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments. ")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv) - 1} argument: ")
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print('{}: {}'.format(len(sys.argv) - 1, arg))
    else:
        print(f"{len(sys.argv) - 1} arguments: ")
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print('{}: {}'.format(i, arg))
