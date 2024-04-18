with open("my_first_file.txt", mode="r+", encoding="UTf-8") as file_:
	"""n = 1
	for line in file_:
		print(f"line {n}:",line, end="")
		n+=1
	file_.write("i am adding the line at the end \n and also this agian")
	"""
	print(file_.read(30))
	print("new.......")
	print(str(file_.readlines()))
	print(file_.write('This is a test\n'))
