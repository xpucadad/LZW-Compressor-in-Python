input = b'It was the best of times, it was the worst of times.'
print(input)
print(input.hex())

pattern_to_index = {}
index_to_pattern = []

output = []
pattern_buffer = bytearray(0)

def store_pattern(pattern):
	index_to_pattern.append(pattern)
	index = len(index_to_pattern) - 1
	pattern_to_index[pattern] = index
	return index

store_pattern(b'')

for current_byte in input:
	pattern_buffer.append(current_byte)
	code = 0
	test_pattern = bytes(pattern_buffer)

	if (test_pattern in pattern_to_index):
		code = pattern_to_index[test_pattern]
		matched_pattern = test_pattern
	else:
		# didn't match - output and add new pattern
		output.append(code)
		output.append(current_byte)

		store_pattern(test_pattern)

print (output)

