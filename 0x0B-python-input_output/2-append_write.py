#!/usr/bin/python3
""" a module defines appending... .."""


def append_write(filename="", text=""):
    """
    Appends the given text to a file (UTF-8 encoded)
     and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The content to append to the file.

    Returns:
        int: The number of characters added.
    """
    try:
        with open(filename, "a", encoding="UTF-8") as file:
            file.write(text)
            return len(text)
    except Exception as ex:
        print(f"Error appending to the file: {ex}")
        return 0

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

