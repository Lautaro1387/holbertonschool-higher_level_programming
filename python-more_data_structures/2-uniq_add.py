#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for elements in my_list:
            if elements not in new_list:
                new_list.append(elements)
    Result = sum(new_list)
    return Result
