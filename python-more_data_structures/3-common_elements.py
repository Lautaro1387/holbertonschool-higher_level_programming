#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)
    set3 = set(set_1) & (set_2)
    list3 = list(set3)
    return list3
