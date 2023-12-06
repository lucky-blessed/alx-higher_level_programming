#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    for key, val in a_dictionary.items():
        if val > best:
            best = val
    for key, val in a_dictionary.items():
        if val == best:
            return key
