from collections import defaultdict

with open('./data.txt') as f:
    data = int(f.read().strip('\n'))

def extract_hundred(number):
    return (number // 100) % 10


def populate_grid(serial_number):
    results = defaultdict(int)

    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial_number
            power_level *= rack_id
            power_level = extract_hundred(power_level)
            power_level -= 5

            results[(x, y)] = power_level
    
    return results


def get_grid_score(grid, x, y, size):
    result = 0
    for x_ in range(x, x+size):
        for y_ in range(y, y+size):
            key = (x_, y_)
            result += grid[key]

    return result


def get_best_square(grid, flexible_size=False):
    high_score = 0
    coords = None
    best_size = None
    
    if not flexible_size:
        min_size = 3
        max_size = 4
    else:
        min_size = 1
        max_size = 301
    for size in range(min_size, max_size):
        for x in range(1, 302 - size):
            for y in range(1, 302 - size):
                score = get_grid_score(grid, x, y, size)
                if score > high_score:
                    high_score = score
                    coords = (x, y)
                    best_size = size

    return coords, best_size


grid = populate_grid(data)
coords_pt1, _ = get_best_square(grid)
coords_pt2, best_size = get_best_square(grid, flexible_size=True)

print('Answer pt1: {},{}'.format(coords_pt1[0], coords_pt1[1]))
print('Answer pt2: {},{},{}'.format(coords_pt2[0], coords_pt2[1], best_size)
