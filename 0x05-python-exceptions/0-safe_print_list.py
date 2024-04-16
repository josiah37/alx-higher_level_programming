#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for m in range(x):
        try:
            print(my_list[m], end="")
            n += 1
        except IndexError:
            break
    print()
    return n


my_list = [1, 2, '3', 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
print("---")
mylist = [1, 2, 3, 4]
x = len(mylist) + 10
safe_print_list(mylist, x)
nb_print = safe_print_list(mylist, x)
print("nb_print: {:d}".format(nb_print))
