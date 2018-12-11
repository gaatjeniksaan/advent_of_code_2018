with open('./data.txt') as f:
    data = f.read().strip('\n')
# data = 'dabAcCaCBAcCcaDA'  # Test data

def reacts(c1, c2):
    if c1.lower() != c2.lower():
        return False
    if c1.isupper() & c2.islower():
        return True
    if c1.islower() & c2.isupper():
        return True
    else:
        return False

def react_polymer(polymer):
    reaction_occured = True
    while reaction_occured:
        # print('initialising new loop, data at start: {}'.format(data))
        reaction_occured = False
        for index, char in enumerate(polymer):
            if len(polymer) - index <= 1:
                continue
            if reacts(char, polymer[index+1]):
                # print('reacts == true')
                # print('data before: {}'.format(data))
                polymer = polymer[:index] + polymer[index+2:]
                reaction_occured = True
                # print('data after: {}'.format(data))
                break
    return polymer

result1 = react_polymer(data)
print('Answer pt1: {}'.format(len(result1)))

length = len(data)
chars = set(data.lower())
for char in chars:
    stripped_data = data.replace(char, '').replace(char.upper(), '')
    reacted = react_polymer(stripped_data)
    if len(reacted) < length:
        length = len(reacted)

print('Answer pt2: {}'.format(length))
