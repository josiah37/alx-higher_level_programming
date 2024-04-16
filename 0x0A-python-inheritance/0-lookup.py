#!/usr/bin/python3
""" Defines an object attribute, a lookup func"""


def lookup(obj):
    """
    A unction that returns the list of
    available attributes and methods of an object
    """
    return (dir(obj))
