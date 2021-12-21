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
    with open(filename) as myfile:
        readfile = myfile.read()
        print(read_file, end="")
    
