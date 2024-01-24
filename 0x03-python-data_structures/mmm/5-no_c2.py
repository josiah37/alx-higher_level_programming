#!/usr/bin/python3

"""
LOOP over every character
If a character == c or C
     pop it out
"""


def no_c(my_string):
    my_string.remove()
    #my_string.remove(C) 
    return my_string


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
    
