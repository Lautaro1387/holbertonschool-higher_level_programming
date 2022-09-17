#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for elements in my_list:
        for elements in new_list:
            if elements not in new_list:
                new_list.append(elements)
    return new_list
