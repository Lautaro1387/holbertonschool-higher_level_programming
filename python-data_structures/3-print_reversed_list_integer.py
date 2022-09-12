#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for number in range(len(my_list)):
        if number < 0:
            return None
        print("{:d}".format(my_list[number]))
