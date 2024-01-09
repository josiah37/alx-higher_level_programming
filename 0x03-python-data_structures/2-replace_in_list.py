#!/usr/bin/python3

"""
* If idx is negative, the function should not modify anything,
  and returns the original list

* If idx is out of range (> of number of element in my_list),
  the function should not modify anything, and returns the original list


               white boarding
list[wz indx to be changed] = the new element
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
