#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original = my_list.copy()
    original[idx] = element
    return original
