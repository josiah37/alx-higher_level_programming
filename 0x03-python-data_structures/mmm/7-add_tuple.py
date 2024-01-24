"""
count the number of tuples in each argument 
compare them and choose the grater one 
add zeros to make it ecuvalent
do the math (adding the 1st argument, adding the 2nd, adding the nth)
"""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
            tuple_a = (0,0)
    elif len(tuple_b) == 0:
            tuple_b = (0,0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
            tuple_a = (tuple_a[0], 0)
            tuple_b = (tuple_b[0], 0)
    elif len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
    new_tuple = ((tuple_a[0] + tuple_b[0]),(tuple_a[1] + tuple_b[1]))
    return new_tuple

x = add_tuple((3,),(7,))
print(x)

"""
if:
if len(tuple_a) or len(tuple_a) == 0:
    tup_tmp((0,0), (0,0))
elif len(tuple_a) == 1:
    tup_tmp((tuple_a[0],0), (0,0))
elif len(tuple_b) == 1:
    tup_tmp((0,0), (0,tuple_b[1]))
tup_tmp = ((tup_tmp[0] + tup_tmp[0]),(tup_tmp[1] + tup_tmp[1])) 
"""
print("\n")
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))




def add_tuple2(tuple_a=(), tuple_b=()):
    """

    if len(tuple_a) == 0:
            tuple_a = (0,0)
    elif len(tuple_b) == 0:
            tuple_b = (0,0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
            tuple_a = (tuple_a[0], 0)
            tuple_b = (tuple_b[0], 0)
    elif len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
     """
    tuple_a =(tuple_a)+ (0,0)
    tuple_b = (tuple_b) + (0,0)
    new_tuple = ((tuple_a[0] + tuple_b[0]),(tuple_a[1] + tuple_b[1]))
    return new_tuple

x = add_tuple((3,),(7,))
print(x)

x = add_tuple((3,),(7,2,3))
print(x)
