#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
"""


#        whiteboarding 
"""
print(matrix[2][2]) ... gives us 9 so we can print them 
all with iteration i think 

for row in matrix:
	for colomen in matrix:
		print(matrix[row][colomen]) 
"""


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for colmn in range(len(matrix[row])):
                print(matrix[row][colmn], end = "")
                if colmn < len(matrix[row])-1:
#                       print(matrix[row][colmn], end = "")
                       print(" ", end="")
        print("")
           



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [3, 5, 6]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
