#!/usr/bin/python3

"""
create a new str
LOOP over every character of my str
If a character == c or C
     update the str with the above indice value
"""


def no_c(my_string):
    my_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            my_str += i
    return my_str


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
print(no_c("Holberton"))    
print(no_c(""))
print(no_c("HellcCcccooccoscccss"))
