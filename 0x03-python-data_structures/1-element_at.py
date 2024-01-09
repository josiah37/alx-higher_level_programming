#!/usr/bin/python3

def element_at(my_list, idx):
    # i replaced the 2 if conditons to wz 1 as the excution is the same
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
