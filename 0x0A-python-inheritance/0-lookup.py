#!/usr/bin/python3
"""
returns list of available attributes and methods of an object
"""


def lookup(obj):
    """
    function: lookup()
    :param obj:
    :return: list of object
    """
    return dir(obj)
