#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_list = my_list[0]
    for number in my_list:
        if number > max_list:
            max_list = number
            return max_list
