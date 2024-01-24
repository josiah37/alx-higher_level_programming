#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))


xx = [1, 2, 3, 4, 5]
print_list_integer(xx)

list = [1, 2, 9]
print_list_integer(list)
