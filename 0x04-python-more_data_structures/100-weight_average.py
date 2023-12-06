#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_total = sum(score * weight for score, weight in my_list)
    weight_total = sum(weight for _, weight in my_list)
    return score_total / weight_total if weight_total != 0 else 0
