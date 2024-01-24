#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return 'None'
    else:
        return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3] 

idx = 1
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = 2
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
idx = 3

print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = -1 
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

list = [1]
idx = 1
print("Element at index {:d} is {}".format(idx, element_at(list, idx)))
#
