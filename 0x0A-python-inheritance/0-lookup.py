#!/usr/bin/python3
""" Defines an object attribute, a lookup func"""


def lookup(obj):
    """
    A unction that returns the list of
    available attributes and methods of an object
    """
    return (dir(obj))


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
