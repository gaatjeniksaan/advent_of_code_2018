with open("./data.txt") as f:
	input = f.readlines()
	data = []
	for i in input:
		data.append(int(i.strip("\n")))

freq = 0

for j in data:
	freq += j

print("Final frequency: ", freq)

# Part 2
freqFound = False
freqMap = {}
freqPt2 = 0
print("before loop freqMap: ", freqMap)

print(freqPt2 in freqMap.keys())
while freqFound == False:
	for k in data:
		if freqPt2 in freqMap.keys():
			print("First frequency to encounter twice: ", freqPt2)
			freqFound = True
			break
		else:
			freqMap[freqPt2] = "present"

		freqPt2 += k
