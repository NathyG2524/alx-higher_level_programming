#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print(f"{len(sys.argv) - 1} arguments. ")
elif len(sys.argv) == 2:
    print(f"{len(sys.argv) -1} argument: ")
else:
    print(f"{len(sys.argv) - 1} arguments: ")
for i  in range(1, len(sys.argv)):
    print('{}: {}'.format(i, sys.argv[i]))
