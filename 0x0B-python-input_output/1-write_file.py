#!/usr/bin/python3

""" a module deines a func that count number of words written"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    return: the number of characters written
    """
    with open(filename, mode="w", encoding="UTF8") as myfile:
        myfile.write(text)
        word_count = len(text)
        return word_count
