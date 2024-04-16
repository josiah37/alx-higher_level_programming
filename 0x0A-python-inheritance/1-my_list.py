#!/usr/bin/python3
""" this module defines a class that inherets form the a super clas 'List' """


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """ prints the list, in  sorted, ascending order """
        sorted_list = sorted(self)
        print(sorted_list)
