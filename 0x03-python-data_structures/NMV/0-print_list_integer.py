#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))


list = [1, 2,'H', 9]
print_list_integer(list)
