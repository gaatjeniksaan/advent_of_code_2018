from collections import defaultdict

with open("./data.txt") as f:
	data = [{
		"id":		x.split()[0],
		"left": 	int(x.split()[2].split(",")[0]),
		"top":		int(x.split()[2].split(",")[1].strip(":")),
		"width": 	int(x.split()[3].split("x")[0]),
		"length":	int(x.split()[3].split("x")[1].strip("\n")),}
		for x in f.readlines()]

coords = defaultdict(list)


for item in data:
	# Get upper right coordinate first
	ul_row = item["top"]
	ul_col = item["left"]

	for row in range(item["length"]):
		for col in range(item["width"]):
			r = ul_row + row
			c = ul_col + col
			coords[(r, c)].append(item["id"])


print("Answer part 1: ", sum(1 for i in coords.values() if len(i) > 1))

ids = set([x["id"] for x in data])
double_ids = set([x for y in coords if len(y) > 1 for x in y])

print(len(ids))
print(len(double_ids))

print("Answer part 2: ", ids.intersection(double_ids))
# 
# for x in coords:


# print(coords)

# print("Answer part 2: ", )


# print(coords)