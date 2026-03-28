#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    s = 0
    for i in new_list:
        if i == search:
            new_list[s] = replace
        s += 1
    return new_list
