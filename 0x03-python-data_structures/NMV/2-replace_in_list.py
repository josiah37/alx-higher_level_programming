#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list


list = [1, 2, 3]
idx = 0
new_element = 4
new_list = replace_in_list(list, idx, new_element)

print(new_list)
print(list)


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)



list = [1, 2, 3]
idx = 2
new_element = 4
new_list = replace_in_list(list, idx, new_element)

print(new_list)
print(list)

"""
list = [1]
idx = 1
new_element = 4
new_list = replace_in_list(list, idx, new_element)

print(new_list)
print(list)
"""



list = [1]
idx = 0
new_element = 4
new_list = replace_in_list(list, idx, new_element)

print(new_list)
print(list)



