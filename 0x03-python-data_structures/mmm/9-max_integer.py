"""
find the len of the string(mebers)
for i in members
	if i[0] <= 
"""
def max_in_list(x=[]):
	for i in range(len(x)-1):
		max_val = x[i]
		if x[i] > max_val:
			max_val = x[i]
	return max_val

n = [3,6,2,73,5]
print(max_in_list(n))
