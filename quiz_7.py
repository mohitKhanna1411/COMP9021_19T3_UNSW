# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.

#checking whether the element is valid element to be coloured
def is_valid_element(grid,x,y):
    if (x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]==1):
        return True
    else:
        return False

#starting with 2 as 0's and 1's are already present in the grid formed
colour = 2

#recursive method to identify a shape using colouring
def colouring(grid, i, j):
    if is_valid_element(grid, i, j):
        grid[i][j] = colour
        #checking upper element
        if not colouring(grid, i-1, j):
            grid[i][j] = 0
        #checking lower element
        elif not colouring(grid, i+1, j):
            grid[i][j] = 0
        #checking left element
        elif not colouring(grid, i, j-1):
            grid[i][j] = 0
        #checking right element
        elif not colouring(grid, i, j+1):
            grid[i][j] = 0
    return colour

#traversing every element to identify shapes
def colour_shapes():
    #globally declared variable
    global colour
    for i in range(dim):
        for j in range(dim):
            if colouring(grid, i, j):
                colour += 1
    return colour

def max_number_of_spikes(nb_of_shapes):
#max number of colours for 10X10 grid is 102

    #12X12 matrix padded_grid
    padded_grid = [[0 for x in range(12)] for x in range(12)]

    #used to identify spikes at the boundary or corner of the matrix
    for i in range(dim):
        for j in range(dim):
            padded_grid[i+1][j+1]=grid[i][j]
    #max spikes from all the shapes in the grid
    max_spkie = 0
    for x in range(2, nb_of_shapes):
        #number of spikes for every shape
        spike = 0
        #nested loop for 12x12 grid
        for i in range(1,dim+1):
            for j in range(1,dim+1):
                #identifying the shape thorugh its colour
                if padded_grid[i][j] == x:
                    #identifying the spike
                    #if the sum of the neighbours is equal to the element itself then its a spike
                    if padded_grid[i-1][j] + padded_grid[i+1][j] + padded_grid[i][j-1] + padded_grid[i][j+1] == x:
                        #spike identified
                        spike += 1
                        #identifying max_spike through maximum logic
                        if spike > max_spkie:
                            max_spkie = spike
    #return final value
    return max_spkie

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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
