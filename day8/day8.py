with open('./data.txt') as f:
    data = f.readlines()
    data = [int(x) for x in data[0].split()]

#data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def func(data):
    n_children = data[0]
    n_metadata = data[1]
    metadata_sum = 0

    # cut off first two entries
    data = data[2:]
    
    for i in range(n_children):
        data, meta = func(data)
        metadata_sum += meta
    
    metadata_sum += sum(data[:n_metadata])

    return data[n_metadata:], metadata_sum

_, answer = func(data)
print('Answer part 1: {}'.format(answer))