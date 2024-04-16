#!/usr/bin/python3

"""
in this module we define a function, inherits_from that checks
 the instace of an object
"""


def inherits_from(obj, a_class):
    """
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class ; otherwise False.
    """
    #   if type(obj).__name__ == a_class.__name__: # type(obj) == a_class:
    if issubclass(type(obj), a_class):
        if type(obj).__name__ != a_class.__name__:
            return (True)
    return (False)
