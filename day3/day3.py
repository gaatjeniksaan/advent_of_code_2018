from collections import defaultdict

with open("./data.txt") as f:
	data = [{
		"id":		x.split()[0],
		"left": 	int(x.split()[2].split(",")[0]),
		"top":		int(x.split()[2].split(",")[1].strip(":")),
		"width": 	int(x.split()[3].split("x")[0]),
		"length":	int(x.split()[3].split("x")[1].strip("\n")),}
		for x in f.readlines()]

coords = defaultdict(int)

for i in range(2):
	# First loop to check populate coordinates and check how many are doubled
	# Second loop to check per ID if they access a coordinate that is a double
	for item in data:
		overlap = False
		# Get upper right coordinate first
		ul_row = item["top"]
		ul_col = item["left"]

		for row in range(item["length"]):
			for col in range(item["width"]):
				r = ul_row + row
				c = ul_col + col
				if i == 1 and coords[(r, c)] > 1:
					overlap = True
					continue
				coords[(r, c)] += 1

		if i == 1 and overlap == False:
			print("Answer part 2: ", item["id"].strip("#"))

	if i == 0:
		print("Answer part 1: ", sum(1 for i in coords.values() if i > 1))
		print("Length of coords: ", len(coords))
