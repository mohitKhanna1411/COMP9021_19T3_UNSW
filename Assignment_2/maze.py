# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10


# IMPORT ANY REQUIRED MODULE

from pathlib import Path
from copy import deepcopy

# Determine the coordinates of the next point based on N, S, W, E
NEIGHBOUR = {
    'N': lambda p: (p[0], p[1] - 1),
    'S': lambda p: (p[0], p[1] + 1),
    'W': lambda p: (p[0] - 1, p[1]),
    'E': lambda p: (p[0] + 1, p[1])
}

# The reverse direction of the points.
OPPOSITION = {
    'S': 'N',
    'N': 'S',
    'W': 'E',
    'E': 'W'
}

class MazeError(Exception):
    def __init__(self, message):
        self.message = message

class MazeInitGrad:
    def __new__(self, x_dim, y_dim, maze, directions):
        # print(f'directions   {directions[3]}')
        grid = [[''] * y_dim for _ in range(x_dim)]
        # print(grid)
        # print("--------grid-----------------")
        for x in range(x_dim):
            for y in range(y_dim):
                # grid_inner_point_no_object[x][y] = directions[self.get_inner_point(x, y)]
                #Traverse the direction that this node can point to
                for d in directions[maze[y][x]]:
                    # print(directions[3])
                    # print(self.maze[y][x])
                    # print(f'd    {d}')
                    #Add the direction that this node can point at once
                    grid[x][y] += d
                    # print(grid[x][y])
                    #Pre is used to receive the coordinates of the next node in the direction 
                    #of the return and the pointing direction of the next node
                    n = NEIGHBOUR[d]
                    # print(n((x, y))[0] , n((x, y))[1])
                    pre = (n((x, y))[0], n((x, y))[1], OPPOSITION[d])
                    # print(pre)
                    if 0 <= pre[0] <= x_dim - 1 and 0 <= pre[1] <= y_dim - 1:
                        #Add the pointing direction of the next node
                        grid[pre[0]][pre[1]] += pre[2]
        return grid

class MazeChildren:
    def __new__(self, x, y, grid):
        children = list()
        direction = grid[x][y]
        for d in direction:
            children.append(NEIGHBOUR[d]((x, y)))
        return children
        
class MazeTraversal:
    def __new__(self, x, y, grid, x_dim, y_dim, x_l=0, x_r=0, y_t=0, y_b=0, *, key=None):
        # Trim the grid and divide it into: left, right, up, down.
        visited_point = set()
        q = list()
        q.append((x, y))
        while len(q):
            p = q.pop()
            visited_point.add(p)
            for c in MazeChildren(p[0], p[1], grid):
                if 0 + x_l <= c[0] <= x_dim - 1 - x_r and 0 + y_t <= c[1] <= y_dim - 1 - y_b:
                    if c not in visited_point:
                        if not key:
                            q.append(c)
                        elif key(c):
                            q.append(c)
        # The returned set contains the starting node itself
        return visited_point

class MazeGates:
    def __new__(self, x_dim, y_dim, grid_inner_point):
        #Traversing the four sides, there is a correspondence (the upper side must have a N-notch, 
        #the lower side should have an S-notch). The gap is the door.
        # Gate third question, ask for accessible area needs
        # Gate structure: ((door X coordinate, gate Y coordinate), (entry X coordinate, entry Y coordinate))
        gate_set = set()
        for i in [(0, 'W'), (x_dim - 2, 'E')]:
            for j in range(y_dim - 1):
                if i[1] in grid_inner_point[i[0]][j]:
                    # print([(0, 'W'), (self.x_dim - 2, 'E')])
                    # print(self.grid_inner_point[i[0]][j])
                    # num_gate += 1
                    gate_set.add(
                        ((i[0], j), NEIGHBOUR[i[1]]((i[0], j)))
                    )
        for i in range(x_dim - 1):
            for j in [(0, 'N'), (y_dim - 2, 'S')]:
                if j[1] in grid_inner_point[i][j[0]]:
                    # num_gate += 1
                    gate_set.add(
                        ((i, j[0]), NEIGHBOUR[j[1]]((i, j[0])))
                    )
                    # print(gate_set)
        return gate_set, len(gate_set)

class MazeWalls:
    def __new__(self, x_dim, y_dim, grid_point):
        # The top left corner begins to traverse the entire point grid (if this point is skipped in the visited), 
        # use the breadth-first traversal to find all the points that are connected or indirectly connected to it
        # and mark them visited
        pillar_set = set()
        num_set_of_wall = 0
        visited_point_for_wall = set()
        # Traversing the entire grid point
        for x in range(x_dim):
            for y in range(y_dim):
                # Skip if the current point already exists in visited
                if (x, y) not in visited_point_for_wall:
                    # Returns all points indirectly connected to this point, including this point
                    vp = MazeTraversal(x, y, grid_point, x_dim, y_dim)
                    # print(x,y,vp, type(vp))
                    # print("-----------------------")
                    # If there is only this point, it means that this is not a wall, this is a pillar
                    if len(vp) == 1:
                        pillar_set = pillar_set.union(vp)
                    # If more than one point is returned, it means a wall
                    else:
                        num_set_of_wall += 1
                        # It is reasonable to write this in it.
                        visited_point_for_wall = visited_point_for_wall.union(vp)

        return pillar_set, num_set_of_wall

class MazeAreas:
    def __new__(self, x_dim, y_dim, gate_set, grid_inner_point):
        num_accessible_area = 0
        visited_inner_point_for_area = set()
        for g in gate_set:
            if g[0] not in visited_inner_point_for_area:
                vip = MazeTraversal(g[0][0], g[0][1], grid_inner_point, x_dim, y_dim, x_r=1, y_b=1)
                visited_inner_point_for_area = visited_inner_point_for_area.union(vip)
                num_accessible_area += 1
        return num_accessible_area, visited_inner_point_for_area

class MazeCulDeSacs:
    def __new__(self, x_dim, y_dim, grid_inner_point, visited_inner_point_for_area):
        # Create a avatar for grid_inner_point
        # Path to use, this is a grid that uses cul-de-sacs as the wall
        grid_inner_point_copied = deepcopy(grid_inner_point)
        # All cul_de_sacs
        cul_de_sacs_set = set()
        # a node with an initial degree of 1
        initial_cul_de_sacs_set = set()
        # First find all the nodes with the degree of 1 in the reachable node and put them in the queue.
        q = list()
        for p in visited_inner_point_for_area:
            if len(grid_inner_point[p[0]][p[1]]) == 1:
                q.append(p)
                initial_cul_de_sacs_set.add(p)

        while len(q):
            # Take one out of the queue
            current_point = q.pop()
            cul_de_sacs_set.add(current_point)
            # Find the neighbor of this node
            next_point = MazeChildren(current_point[0], current_point[1], grid_inner_point_copied)[0]
            if 0 <= next_point[0] <= x_dim - 2 and 0 <= next_point[1] <= y_dim - 2:
                # Change the direction of adjacent nodes
                grid_inner_point_copied[next_point[0]][next_point[1]] = grid_inner_point_copied[next_point[0]][next_point[1]].replace(
                        OPPOSITION[grid_inner_point_copied[current_point[0]][current_point[1]]],
                        ''
                    )
                # If the current node also becomes a node with a degree of 1, it is placed in the queue.
                if len(grid_inner_point_copied[next_point[0]][next_point[1]]) == 1:
                    q.append(next_point)
            # Change the direction of this node
            grid_inner_point_copied[current_point[0]][current_point[1]] = ''

        num_cul_de_sacs_set = 0
        visited_inner_point_for_cul_de_sacs = set()
        for cul in sorted(initial_cul_de_sacs_set):
            if cul not in visited_inner_point_for_cul_de_sacs:
                visited_inner_point_for_cul_de_sacs = visited_inner_point_for_cul_de_sacs.union( MazeTraversal(
                    cul[0], cul[1], grid_inner_point, x_dim, y_dim, x_r=1, y_b=1,
                    key=lambda arg: arg in cul_de_sacs_set
                ))
                num_cul_de_sacs_set += 1
        return grid_inner_point_copied, cul_de_sacs_set, num_cul_de_sacs_set

class MazePath:
    def __new__(self, x_dim, y_dim, gate_set,cul_de_sacs_set, grid_inner_point_trimmed):
        visited_inner_point_for_path = set()
        entry_exit_path_list = list()
        entry_exit_path_set = set()
        for g in gate_set:
            # If this door is not cul-de-sacs nor visited
            if g[0] not in cul_de_sacs_set and g[0] not in visited_inner_point_for_path:
                visited_point_list = list()
                visited_point_set = set()
                bfs_q = list()
                bfs_q.append(g[0])
                dirty = False
                while len(bfs_q):
                    bfs_p = bfs_q.pop()
                    if len(grid_inner_point_trimmed[bfs_p[0]][bfs_p[1]]) != 2:
                        dirty = True
                    else:
                        visited_point_list.append(bfs_p)
                    visited_point_set.add(bfs_p)
                    for c in MazeChildren(bfs_p[0], bfs_p[1], grid_inner_point_trimmed):
                        if c not in visited_point_set:
                            if 0 <= c[0] <= x_dim - 2 and 0 <= c[1] <= y_dim - 2:
                                bfs_q.append(c)
                if not dirty:
                    entry_exit_path_list.append(visited_point_list)

                    # Find the first and last line of the line and do the union directly
                    visited_point_set = visited_point_set.union(
                        set(
                            MazeChildren(
                                visited_point_list[0][0],
                                visited_point_list[0][1],
                                grid_inner_point_trimmed
                            )
                        ))

                    visited_point_set = visited_point_set.union(
                        set(
                           MazeChildren(
                                visited_point_list[-1][0],
                                visited_point_list[-1][1],
                                grid_inner_point_trimmed
                            )
                        ))

                    entry_exit_path_set = entry_exit_path_set.union(visited_point_set)
                visited_inner_point_for_path = visited_inner_point_for_path.union(visited_point_set)
        return len(entry_exit_path_list), entry_exit_path_set
        
class Maze:
    def __init__(self, filename):
        self.file_path = Path(filename)
        with open(self.file_path) as f:
            lines = f.read().splitlines()
        #Looking for length
        length = 0
        maze = []
        for line in lines:
            #Remove spaces
            line = line.replace(' ', '')
            #If the current line is not a blank line
            if len(line):
                #If the length of length is 0, assign the length of the current line to length
                if not length:
                    length = len(line)
                #If length is not already 0, compare whether the length of the current line
                #is equal to the previous length, and if it is not equal to throw an exception
                elif len(line) != length:
                    #Two lines are not equal in length
                    raise MazeError('Incorrect input.')
                #See if the number in the current line exceeds the range
                if length > 31 or length < 2:
                    #print(f'number per line exceeds {length}')
                    raise MazeError('Incorrect input.')
                elements = []
                #str -> int & separate numbers
                for i in line:
                    if i in {'0', '1', '2', '3'}:
                        elements.append(int(i))
                        # print(f'elements {elements}')
                    #If it is not the number, throw an exception
                    else:
                        # print('Number does not exist {0,1,2,3}')
                        raise MazeError('Incorrect input.')
                #The last bit of each line cannot be 1 or 3
                if elements[-1] == 1 or elements[-1] == 3:
                    raise MazeError('Input does not represent a maze.')
                maze.append(elements)
                # print(f'maze {maze}')
            #Determine how many rows are currently in use
            if len(maze) > 41:
                raise MazeError('Incorrect input.')
        #Determine whether the minimum number of rows 
        #allowed is reached after all loading is completed.
        if len(maze) < 2:
            # print(f'The number of lines is too small, {len(maze)}')
            raise MazeError('Incorrect input.')
        #The last line cannot be 2 or 3
        if 2 in maze[-1] or 3 in maze[-1]:
            raise MazeError('Input does not represent a maze.')
        #Grid raw data
        self.maze = maze
        #Horizontal length of the grid
        self.x_dim = length
        #Length of the grid
        self.y_dim = len(maze)

        #When the inner point corresponding to the current point is 0, 
        #the point is not connected to any point.
        directions_of_point = {
            0: '',
            1: 'E',
            2: 'S',
            3: 'SE'
        }
        #When the current inner point is 0, the inner point must be connected to N and W. 
        #as to whether it can be connected to S and E, the value of this point can be determined.
        directions_of_inner_point = {
            0: 'NW',
            1: 'W',
            2: 'N',
            3: ''
        }

        #Point and inner point matrix
        self.grid_point = MazeInitGrad(self.x_dim, self.y_dim, self.maze, directions_of_point)
        self.grid_inner_point = MazeInitGrad(self.x_dim, self.y_dim, self.maze, directions_of_inner_point)

        # ------------GATE----------------
        self.gate_set, self.num_gate = MazeGates(self.x_dim, self.y_dim, self.grid_inner_point)
        # ------------END GATE------------

        # ------------WALL----------------
        self.pillar_set, self.num_set_of_wall = MazeWalls(self.x_dim, self.y_dim, self.grid_point)
        # ------------END WALL------------

        # ------------ACCESSIBLE AND INACCESSIBLE AREA------------------
        self.num_accessible_area, self.visited_inner_point_for_area = MazeAreas(self.x_dim, self.y_dim, self.gate_set, self.grid_inner_point)
        self.num_inaccessible_inner_point = (self.y_dim - 1) * (self.x_dim - 1) - len(self.visited_inner_point_for_area)
        # ------------END ACCESSIBLE AND INACCESSIBLE AREA--------------

        # ------------CUL-DE-SACS----------------
        # Trimmed grid_inner_point
        # Collection of cul_de_sacs, display needs to be used
        self.grid_inner_point_trimmed, self.cul_de_sacs_set, self.num_cul_de_sacs_set = MazeCulDeSacs(self.x_dim, self.y_dim, self.grid_inner_point, self.visited_inner_point_for_area)
        # ------------END CUL-DE-SACS------------

        # ------------PATH----------------
        self.num_entry_exit_path, self.entry_exit_path_set = MazePath(self.x_dim, self.y_dim, self.gate_set, self.cul_de_sacs_set, self.grid_inner_point_trimmed)
        # ------------END PATH------------

    def analyse(self):
        
        gate_output_dict = {
            0: 'no gate.',
            1: 'a single gate.'
        }
        print(f'The maze has {gate_output_dict.get(self.num_gate, f"{self.num_gate} gates.")}')

        wall_output_dict = {
            0: 'no wall.',
            1: 'walls that are all connected.'
        }
        print(f'The maze has '
              f'{wall_output_dict.get(self.num_set_of_wall,f"{self.num_set_of_wall} sets of walls that are all connected.")}')

        inaccessible_point_output_dict = {
            0: 'no inaccessible inner point.',
            1: 'a unique inaccessible inner point.'
        }
        t_str_for_area_output = f"{self.num_inaccessible_inner_point} inaccessible inner points."
        print(f'The maze has '
              f'{inaccessible_point_output_dict.get(self.num_inaccessible_inner_point, t_str_for_area_output)}')

        accessible_area_output_dict = {
            0: 'no accessible area.',
            1: 'a unique accessible area.'
        }
        print(f'The maze has '
              f'{accessible_area_output_dict.get(self.num_accessible_area, f"{self.num_accessible_area} accessible areas.")}')

        cul_de_sacs_output_dict = {
            0: 'no accessible cul-de-sac.',
            1: 'accessible cul-de-sacs that are all connected.'
        }
        t_str_for_cul_output = f'{self.num_cul_de_sacs_set} sets of accessible cul-de-sacs that are all connected.'
        print(f'The maze has {cul_de_sacs_output_dict.get(self.num_cul_de_sacs_set, t_str_for_cul_output)}')

        entry_exit_path_output_dict = {
            0: 'no entry-exit path with no intersection not to cul-de-sacs.',
            1: 'a unique entry-exit path with no intersection not to cul-de-sacs.'
        }
        t_str_for_path_output = f'{self.num_entry_exit_path} entry-exit paths with no intersections not to cul-de-sacs.'
        print(f'The maze has {entry_exit_path_output_dict.get(self.num_entry_exit_path, t_str_for_path_output)}')

    def display(self):
        tex_content_head = '\\documentclass[10pt]{article}\n' \
                           '\\usepackage{tikz}\n' \
                           '\\usetikzlibrary{shapes.misc}\n' \
                           '\\usepackage[margin=0cm]{geometry}\n' \
                           '\\pagestyle{empty}\n' \
                           '\\tikzstyle{every node}=[cross out, draw, red]\n' \
                           '\n' \
                           '\\begin{document}\n' \
                           '\n' \
                           '\\vspace*{\\fill}\n' \
                           '\\begin{center}\n' \
                           '\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n'

        tex_content_tail = '\\end{tikzpicture}\n' \
                           '\\end{center}\n' \
                           '\\vspace*{\\fill}\n' \
                           '\n' \
                           '\\end{document}\n'

        # ----------WALL----------
        tex_content_walls = list()
        tex_content_walls.append('% Walls\n')
        for y in range(self.y_dim):
            x = 0
            while x <= self.x_dim - 1:
                if 'E' not in self.grid_point[x][y]:
                    x += 1
                    continue
                tmp = list()
                tmp.append((x, y))
                for t in range(x + 1, self.x_dim):
                    if 'E' not in self.grid_point[t][y]:
                        tmp.append((t, y))
                        x = t + 1
                        break
                tex_content_walls.append(f'    \\draw ({tmp[0][0]},{tmp[0][1]}) -- ({tmp[1][0]},{tmp[1][1]});\n')
        for x in range(self.x_dim):
            y = 0
            while y <= self.y_dim - 1:
                if 'S' not in self.grid_point[x][y]:
                    y += 1
                    continue
                tmp = list()
                tmp.append((x, y))
                for t in range(y + 1, self.y_dim):
                    if 'S' not in self.grid_point[x][t]:
                        tmp.append((x, t))
                        y = t + 1
                        break
                tex_content_walls.append(f'    \\draw ({tmp[0][0]},{tmp[0][1]}) -- ({tmp[1][0]},{tmp[1][1]});\n')
        # ----------END WALL----------

        # ----------PILLAR----------
        tex_content_pillars = list()
        tex_content_pillars.append('% Pillars\n')
        for pillar in sorted(self.pillar_set, key=lambda p: (p[1], p[0])):
            tex_content_pillars.append(f'    \\fill[green] ({pillar[0]},{pillar[1]}) circle(0.2);\n')
        # for y in range(self.y_dim):
        #     for x in range(self.x_dim):
        #         if self.grid_point[x][y] == '':
        #             tex_content_pillars.append(f'    \\fill[green] ({x},{y}) circle(0.2);\n')
        # ----------END PILLAR----------

        # ----------CUL-DE-SACS----------
        tex_content_cul_de_sacs = list()
        tex_content_cul_de_sacs.append('% Inner points in accessible cul-de-sacs\n')
        for i in sorted(self.cul_de_sacs_set, key=lambda s: (s[1], s[0])):
            tex_content_cul_de_sacs.append(f'    \\node at ({i[0]+0.5},{i[1]+0.5}) ''{};\n')
        # ----------END CUL-DE-SACS----------

        # ----------ENTRY-EXIT PATH----------
        tex_content_entry_exit_path = list()
        tex_content_cul_de_sacs.append(f'% Entry-exit paths without intersections\n')
        for y in range(self.y_dim - 1):
            tmp_path_list = []
            x = self.x_dim - 1
            while x >= 0:
                if (x, y) not in self.entry_exit_path_set or 'W' not in self.grid_inner_point_trimmed[x][y]:
                    x -= 1
                    continue
                tmp = list()
                tmp.append((x, y))
                t = x - 1
                while t >= 0:
                    if 'W' not in self.grid_inner_point_trimmed[t][y]:
                        break
                    t -= 1
                tmp.append((t, y))
                x = t - 1
                tmp_path_list.append(
                    '    \\draw[dashed, yellow] '
                    f'({tmp[1][0]+0.5},{tmp[1][1]+0.5}) -- ({tmp[0][0]+0.5},{tmp[0][1]+0.5});\n')
            tex_content_entry_exit_path.extend(tmp_path_list[::-1])

        for x in range(self.x_dim - 1):
            tmp_path_list = []
            y = self.y_dim - 1
            while y >= 0:
                if (x, y) not in self.entry_exit_path_set or 'N' not in self.grid_inner_point_trimmed[x][y]:
                    y -= 1
                    continue
                tmp = list()
                tmp.append((x, y))
                t = y - 1
                while t >= 0:
                    if 'N' not in self.grid_inner_point_trimmed[x][t]:
                        break
                    t -= 1
                tmp.append((x, t))
                y = t - 1
                tmp_path_list.append(
                    '    \\draw[dashed, yellow] '
                    f'({tmp[1][0]+0.5},{tmp[1][1]+0.5}) -- ({tmp[0][0]+0.5},{tmp[0][1]+0.5});\n')
            tex_content_entry_exit_path.extend(tmp_path_list[::-1])
        # ----------END ENTRY-EXIT PATH----------

        with open(self.file_path.parent / (self.file_path.stem + '.tex'), mode='w') as f:
            f.write(tex_content_head)
            f.writelines(tex_content_walls)
            f.writelines(tex_content_pillars)
            f.writelines(tex_content_cul_de_sacs)
            f.writelines(tex_content_entry_exit_path)
            f.write(tex_content_tail)
