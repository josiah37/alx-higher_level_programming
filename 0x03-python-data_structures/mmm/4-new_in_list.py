#!/usr/bin/python3

"""
copy list
do the replace in the new list
          newlist[index] = element
"""

def new_in_list(my_list, idx, element):
        newlist = my_list.copy()
        newlist[idx] = element
        return newlist


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
    
