#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = []
    for i in range(list_length):
        result = 0
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            result = elem_1 / elem_2
        except (ZeroDivisionError, TypeError):
            if type(elem_1) not in (int, float) or type(elem_2) not in (int, float):
                print("wrong type")
            elif elem_2 == 0:
                print("division by 0")
            else:
                print("out of range")
        finally:
            ret_list.append(result)
    return ret_list
