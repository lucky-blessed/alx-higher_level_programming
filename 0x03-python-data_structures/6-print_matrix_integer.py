#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rw in matrix:
        for x, y in enumerate(rw):
            if x != 0:
                print(" ", end="")
            print("{:d}".format(y), end="")
        print()
