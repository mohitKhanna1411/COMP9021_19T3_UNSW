# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys
from copy import deepcopy

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def get_size(matrix, length, breadth):
    A = deepcopy(matrix)
    first_row = deepcopy(A[0])
    max_size = 0
    for i in range(1, length):
        for j in range(breadth):
            if A[i][j] == 1:
                first_row[j] = first_row[j] + 1
            else:
                first_row[j] = 0
        for x in range(2, length+1):
            L = 0
            for y in range(breadth):
                if first_row[y] >= x:
                    L = L+1
                else:
                    L = 0
                size = 0
                if L >= 2:
                    size = x * L
                if size > max_size:
                    max_size = size
    return max_size

def size_of_largest_parallelogram():
    max_size = get_size(grid, 10, 10)
    grid_right_shift=[[0 for x in range(20)] for x in range(10)]
    for i in range(dim):
        for j in range(dim):
           grid_right_shift[i][j+i]=grid[i][j]
    grid_right_shift_max_size=get_size(grid_right_shift, 10, 20)
    if grid_right_shift_max_size > max_size:
        max_size = grid_right_shift_max_size
    grid_left_shift=[[0 for x in range(20)] for x in range(10)]
    for i in range(dim):
        for j in range(dim):
            grid_left_shift[i][j+dim-i]=grid[i][j]
    grid_left_shift_max_size=get_size(grid_left_shift, 10, 20)
    if grid_left_shift_max_size > max_size:
        max_size = grid_left_shift_max_size
    return max_size

try:
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
