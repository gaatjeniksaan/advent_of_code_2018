from collections import Counter

with open("./data.txt") as f:
	data = [x.strip("\n") for x in f.readlines()]

def count_letter_occurence(seq):
	c = Counter(seq)
	return set(c.values())

counter = Counter()
for seq in data:
	counter.update(count_letter_occurence(seq))
print("Answer part 1: {}".format(counter[2] * counter[3]))

# Part 2
def find_duplicate(seq, data):
	data_copy = data.copy()
	data_copy.remove(seq)  # We don't want to match with the input itself

	for d in data_copy:
		diff = 0
		for index, char in enumerate(d):
			if char != seq[index]:
				diff += 1

		if diff	== 1:
			return seq, d
	
	return None, None

count = 0
for d in data:
	a, b = find_duplicate(d, data)
	if a:
		answer = ""
		for index, char_a in enumerate(a):
			if char_a == b[index]:
				answer += char_a
		print("Answer part 2: {}".format(answer))
		break

