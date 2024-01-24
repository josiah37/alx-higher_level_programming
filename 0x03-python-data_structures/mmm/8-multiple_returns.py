def multiple_returns(sentence):
	w_count = len(sentence)
	if len(sentence) == 0:
		letter = None
	else:
		letter = sentence[0]				
	# making it a tuple
	count_n_letter = w_count, letter
	return(count_n_letter)

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

sentence = "H"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
