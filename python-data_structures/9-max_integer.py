#!/usr/bin/python3
def max_integer(my_list=[]):
    max_list = my_list[0]
    for number in my_list:
        if number == 0:
            return None
        if my_list == 0:
            return None
        if number > max_list:
            max_list = number
            return max_list
