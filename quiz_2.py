# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint
from collections import defaultdict

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
# INSERT YOUR CODE HERE
if keys:
    visited = []
    for key in keys:
        if key in visited:
            continue
        value = mapping.get(key)
        if key == value:
            cycles.append([key])
            visited.append(key)
        else:
            new_items = [key, value]
            while value in mapping:
                new_key = value
                value = mapping.get(new_key)
                if new_items[0] == value:
                    cycles.append(new_items)
                    visited.extend(new_items)
                    break

                if value in new_items:
                    break
                new_items.append(value)

rev_multidict = dict()
for key, value in mapping.items():
    rev_multidict.setdefault(value, list()).append(key)

length_of_values = set([len(values) for key, values in rev_multidict.items()])
reversed_dict_per_length = {}

for val in length_of_values:
    temp_dict = dict()
    for key,value in rev_multidict.items():
        if val == len(value):
             temp_dict[key] = value
    reversed_dict_per_length[val] = temp_dict

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
