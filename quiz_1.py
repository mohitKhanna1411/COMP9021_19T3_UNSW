# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
mapping_as_a_list = [mapping.get(i) for i in range(0, upper_bound)]
one_to_one_part_of_mapping = {}

rev_multidict = {}

for key, value in mapping.items():
    rev_multidict.setdefault(value, set()).add(key)

occurred = set([key for key, values in rev_multidict.items() if len(values) > 1])

for k in sorted(mapping):
    val = mapping[k]
    if val not in occurred:
        one_to_one_part_of_mapping[k] = val
        
nonkeys = [i for i in range(1, upper_bound) if i not in mapping]

# INSERT YOUR CODE HERE

print()
print('EDIT THIS PRINT STATEMENT')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


