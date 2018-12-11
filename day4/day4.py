from collections import defaultdict, Counter

with open('./data.txt') as f:
    data = sorted([x.strip('\n') for x in f.readlines()])

# First let's find the guard that sleeps the most - absolute
gt = defaultdict(list)
for i in data:
    time = int(i.split()[1][3:5])
    if 'Guard' in i:
        is_asleep = False
        guard_id = i.split(' ')[3]
    if 'falls asleep' in i:
        is_asleep = True
        bedtime = time
    if 'wakes up' in i:
        is_asleep = False
        wakeup = time
        for t in range(wakeup - bedtime):
            gt[guard_id].append(bedtime + t)

sleepiest_id = sorted([(len(v), k) for k, v in gt.items()], reverse=True)[0][1]
sleepiest_minute = Counter(gt[sleepiest_id]).most_common()[0][0]
print('Answer pt1: {}'.format(int(sleepiest_id.strip('#')) * sleepiest_minute))

times = 0
sleepiest_guard = None
sleepiest_minute = None
for guard, minutes in gt.items():
    times_asleep = Counter(minutes).most_common()[0][1]
    if times_asleep > times:
        times = times_asleep
        sleepiest_guard = guard
        sleepiest_minute = Counter(minutes).most_common()[0][0]

print('Answer pt2: {}'.format(int(sleepiest_guard.strip('#')) * sleepiest_minute))
