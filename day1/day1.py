import time
from itertools import cycle

with open("./data.txt") as f:
	data = [int(x) for x in f.readlines()]

print("Final frequency: ", sum(data))

# Part 2, let's try out some different scenarios
# Start with a set
frequencies = set()
f = 0

setstart = time.time() 
for i in cycle(data):
	if f in frequencies:
		print("SET. First frequency to encounter twice: ", f)
		break

	frequencies.add(f)
	f += i
setend = time.time()

# Next up: list
frequencies = []
f = 0

liststart = time.time()
for i in cycle(data):
	if f in frequencies:
		print("LIST. First frequency to encounter twice: ", f)
		break

	frequencies.append(f)
	f += i
listend = time.time()

# Final: dict
frequencies = {}
f = 0

dictstart = time.time()
for i in cycle(data):
	if f in frequencies.keys():
		print("DICT. First frequency to encounter twice: ", f)
		break

	frequencies[f] = 1
	f += i
dictend = time.time()

print("Set time in sec: {:0.2f}".format(setend - setstart))
print("List time in sec: {:0.2f}".format(listend - liststart))
print("Dict time in sec: {:0.2f}".format(dictend - dictstart))

