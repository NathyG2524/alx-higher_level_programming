#!/usr/bin/python3
"""
write to a file
"""


def write_file(filename="", text=""):
    """
    functon: write_file
    :param filename:
    :param text:
    :return:
    """
    with open(filename, "w+") as f:
        return f.write(text)
