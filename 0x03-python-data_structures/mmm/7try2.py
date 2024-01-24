def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    # Return a tuple with the addition of corresponding elements
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

# Example usage:
x = add_tuple((3, 8), (2,))
print(x)
