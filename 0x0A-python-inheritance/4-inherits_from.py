#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """
    function: inherits_from()
    :param obj:
    :param a_class:
    :return: True or False
    """
    return not (not isinstance(obj, a_class) or not (type(obj) != a_class))
