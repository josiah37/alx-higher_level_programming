def add_tuple(tuple_a=(), tuple_b=()):
    tup_tmp = None  # Initialize tup_tmp before using it
    
        if len(tuple_a) == 0 or len(tuple_a) == 1:
            tup_tmp = (0, 0)
        if len(tuple_a) == 1:
                tup_tmp = (tuple_a[0], 0)
        elif len(tuple_b) == 1:
            tup_tmp = (0, tuple_b[1])

        # Use tup_tmp in the calculation
        tup_tmp = (tup_tmp[0] + tup_tmp[0], tup_tmp[1] + tup_tmp[1])

    :
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple
# Example usage:
x = add_tuple((3, 8), (2,))
print(x)
