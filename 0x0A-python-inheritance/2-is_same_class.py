#!/usr/bin/python3
""" This module defines a function is_same_class that check if
an instance is belong to a given class or not """


def is_same_class(obj, a_class):
    """
    function that returns True if the object is
    exactly an instance of the specified class; Otherwise False.
    """

    if type(obj).__name__ == a_class.__name__:
        return (True)
    return (False)  # we dont have to use else since the func already ends if
#                     the above ia true
