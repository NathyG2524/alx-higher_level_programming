#!/usr/bin/python3
"""
From JSON string to object
"""


import json


def from_json_string(my_str):
    """
    function: from_json_string()
    :param my_str:
    :return:
    """
    return json.loads(my_str)
