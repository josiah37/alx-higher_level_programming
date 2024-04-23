#!/usr/bin/python3
""" THIS MODULE DEFINES A BASE CALSS FOR ALL OTHER CLASSES"""

class Base:
    """
    a base class for all other classis in the dirctory
    private attribute: __nb_onjects
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not  None:
            self.id = id
        if id is  None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
