#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    second_mtrx = []
    for rw in matrix:
        new_rw = []
        for elm in rw:
            new_rw.append(elm ** 2)
        second_mtrx.append(new_rw)
    return second_mtrx
