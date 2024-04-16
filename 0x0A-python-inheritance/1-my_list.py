#!/usr/bin/python3
""" this module defines a class that inherets form the a super clas 'List' """


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """ prints the list, in  sorted, ascending order """
        sorted_list = sorted(self)
        print(sorted_list)

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
#my_list.append(None)
#my_list.append(int)
print(my_list)
my_list.print_sorted()
print(my_list)
