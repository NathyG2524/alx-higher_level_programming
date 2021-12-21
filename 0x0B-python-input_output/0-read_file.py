#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """
    function: read_file():
    :param filename:
    :return:
    """
    with open(filename) as file:
        readfile = file.read()
        print(readfile, end="")
