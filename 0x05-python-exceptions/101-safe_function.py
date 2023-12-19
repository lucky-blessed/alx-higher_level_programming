#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        outcome = fct(*args)
        return outcome
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
