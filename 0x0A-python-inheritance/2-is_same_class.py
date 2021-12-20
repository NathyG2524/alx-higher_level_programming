#!/usr/bin/python3
"""
a function checks instance of an object
"""


def is_same_class(obj, a_class):
    """
    function:is_same_class
    :param obj:
    :param a_class:
    :return: True or False
    """
    return type(obj) == a_class
