#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_list.reverse()
    if my_list:
        for number in range(len(my_list)):
            print("{:d}".format(my_list[number]))
