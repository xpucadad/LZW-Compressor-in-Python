input = b'It was the best of times, it was the worst of times.'
print(input)
print(input.hex())

dictionary = {}
dict_next_index = 0
dictionary[b''] = 0
pattern = []
output = []
test_pattern= []

for symbol in input:
	test_pattern = pattern
	test_pattern.append(symbol)	


# can't use immutable object as dictianry key


	if (tp in dictionary):
		pattern = test_pattern

	else:
		output.append(dictionary[pattern])
		output.append(symbol)
		dictionary[test_pattern] = dict_next_index
		dict_next_index += 1

print (output)
print (output.hex())

