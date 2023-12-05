#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent > 0:
        first_ch = sentence[0]
    else:
        None
    return (lent, first_ch)
