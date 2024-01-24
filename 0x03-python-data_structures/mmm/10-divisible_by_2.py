def divisible_by_2(my_list=[]):
	list_s = []
	for i in my_list:
		if i % 2 == 0:
			i =True
		else:
			i =  False
		list_s.append(i)
	return list_s



my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
# we know that 0 is always false and other no is True
i = 0

while i < len(list_result):
	print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
	i += 1

print("\n --    other version --\n")


for n,i in zip(my_list,list_result):
	if i == True:
		print(n,"is divisible by 2")
	else:
		print(n,"is not divisible by 2")

print("\n --	other version --\n")

for i in range(len(my_list)):
    if list_result[i]:
        print(my_list[i], "is divisible by 2")
    else:
        print(my_list[i], "is not divisible by 2")

print("\n --    other version --\n")
