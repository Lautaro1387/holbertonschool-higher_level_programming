#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for elements in range(len(new_list)):
        if new_list[elements] == search:
            new_list.remove(search)
            new_list.insert(elements, replace)
    return new_list
    
