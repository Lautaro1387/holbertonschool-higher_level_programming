#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_list = my_list[0]
        for number in range(len(my_list)):
            if my_list[number] > max_list:
                max_list = my_list[number]
        return max_list
