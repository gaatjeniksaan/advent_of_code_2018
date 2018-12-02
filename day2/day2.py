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
