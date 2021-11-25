#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    copy_dic = a_dictionary.copy()
    copy_dic[key] = value
    return copy_dic
