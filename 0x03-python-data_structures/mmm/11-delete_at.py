def delete_at(ll=[], idx=0):
	if 0 >  idx or idx > (len(ll) - 1):
		return ll
	else: 
		del ll[idx]
		return ll


# test cases
n =[2, 6, 3, 8, 3, 4, 5]
print(delete_at(n,8))

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

list = [1, 2, 3, 4, 5]
idx = 5
new_list = delete_at(list, idx)
print(new_list)
print(list)


idx = -1
new_list = delete_at(list, idx)
print(new_list)
print(list)

list = []
idx = 0
new_list = delete_at(list, idx)
print(new_list)
print(list)
