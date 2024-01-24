x = [3,5,7,52,51, 7,9,11]
print("the orginal list is: ", x,"\n")

###
for index, ele in enumerate(x, 1):
	print("{}. {}".format(index, ele))


for i in x:
    print("\t",i+2)


for i in range(len(x) - 1):
    print("\t\t",x[i])


###
x.reverse()
print("\ni reversed the list as:", x)

### copy 

n = x.copy()
print("\nthis is what i copied from 'x' list:", n)

###

even_no = [4,6,8,2,10,16]

print("orginal list:", even_no)
even_no.sort(reverse= True)
print("reversed order:", even_no)
even_no.sort() # defalt is the normal order
print("normal order",even_no)
even_no[-1] = 14
print ("replacing 16 wz 14:", even_no)
