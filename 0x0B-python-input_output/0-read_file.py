#!/usr/bin/python3
""" this module defines a function,read_file, that opens a file """


def read_file(filename=""):
    """
    opens a file with with keyword
    param: filename: is the file we want to open
    """
    with open(filename, mode="r", encoding="UTF8") as myfile:
        print(myfile.read())
