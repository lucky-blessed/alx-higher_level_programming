#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_set = []
    for elem in set_1 & set_2:
        com_set.append(elem)

    return com_set
