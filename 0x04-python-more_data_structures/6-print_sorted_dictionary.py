#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict_key = sorted(a_dictionary.keys())
    for k in sorted_dict_key:
        print("{}: {}".format(k, a_dictionary[k]))
