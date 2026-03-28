#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_ = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list_
    my_list_[idx] = element
    return my_list_
