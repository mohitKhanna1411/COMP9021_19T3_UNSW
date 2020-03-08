# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
from collections import defaultdict

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
octal_number = '0' * nb_of_leading_zeroes + f'{int(code):o}'
matrix = defaultdict(int)
switch = {0: off,1: on}


def flip_switch(points):
    matrix[points] = 0 ** matrix[points]

p = (0, 0)
flip_switch(p)

steps = {0: lambda coordinate: (coordinate[0], coordinate[1]+1),
         1: lambda coordinate: (coordinate[0]+1, coordinate[1]+1),
         2: lambda coordinate: (coordinate[0]+1, coordinate[1]),
         3: lambda coordinate: (coordinate[0]+1, coordinate[1]-1),
         4: lambda coordinate: (coordinate[0], coordinate[1]-1),
         5: lambda coordinate: (coordinate[0]-1, coordinate[1]-1),
         6: lambda coordinate: (coordinate[0]-1, coordinate[1]),
         7: lambda coordinate: (coordinate[0]-1, coordinate[1]+1)
         }

for i in reversed(octal_number):
    p = steps[int(i)](p)
    flip_switch(p)

row = sorted((i[0][0] for i in matrix.items() if i[1] == 1))
column = sorted((i[0][1] for i in matrix.items() if i[1] == 1))

if len(column) != 0 and len(row) != 0:
    top_most, bottom_most = column[len(column) -1], column[0]
    left_most, right_most = row[0], row[len(row) -1]

    for y in range(top_most,bottom_most-1,-1):
        for x in range(left_most, right_most+1):
            print(switch[matrix[(x, y)]], end = ' ')
        print(end = '\n')
