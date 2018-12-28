from collections import Counter, defaultdict

with open('./data.txt') as f:
    data = f.read().strip('\n')
    data = [(int(x.split(', ')[0]), int(x.split(', ')[1])) for x in data.split('\n')]
# test data
# data = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

def get_mhd(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_largest_coords(data):
    x_max = max([x[0] for x in data])
    y_max = max([y[1] for y in data])
    return x_max, y_max


# def get_closest_point(data, x, y):
#     results = defaultdict(list)
#     for index, val in enumerate(data):
#         mhd = get_mhd(x, y, val[0], val[1])
#         results[mhd].append(index)

#     closest = results[sorted(results.keys())[0]]
#     if len(closest) > 1:
#         return None
#     else:
#         return closest[0]


x_max, y_max = get_largest_coords(data)
# results = defaultdict(int)
# infinites = []
# for x in range(x_max + 1):
#     for y in range(y_max + 1):
#         closest = get_closest_point(data, x, y)
#         results[closest] += 1
#         if x == 0 or y == 0 :
#             infinites.append(closest)
#         if x == x_max or y == y_max:
#             infinites.append(closest)

# infinites = set(infinites)
# for i in infinites:
#     results.pop(i)

# print('Answer pt1: {}'.format(sorted(results.values())[-1]))

# What is the size of the region containing all locations which have a 
# total distance to all given coordinates of less than 10000?

def get_total_distance(x, y, data):
    total = 0
    for coord in data:
        mhd = get_mhd(x, y, coord[0], coord[1])
        total += mhd
    
    if total < 10000:
        return 1
    else:
        return 0

result_pt2 = 0
for x in range(x_max):
    for y in range(y_max):
        result_pt2 += get_total_distance(x, y, data)

print('Answer pt2: {}'.format(result_pt2))


