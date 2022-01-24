__author__ = "Akriti Dhasmana, Edward Baptiste, Manav Bilakhia, and Luka Mgaloblishvili"
__copyright__ = "Copyright 2021, Union College Robotics Crew"
__credits__ = ["Akriti Dhasmana", "Edward Baptiste", "Manav Bilakhia", "Luka Mgaloblishvili"]
__version__ = "1.0.1"
__maintainer__ = "Akriti Dhasmana"
__email__ = "dhasmana@union.edu"
__status__ = "Development"

from API import *
import sys
import copy


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()
SIZE = 16
N = 0
E = 1
S = 2
W = 3
#NSEW
MOUSE_DIR = N
grid = []
pos = (15, 0)
curr_flood_val = 14
prev_cell = []
def createGrid():
    # create empty grid
    global grid
    # check if size is odd or even
    if SIZE % 2 == 0:

        for i in range(0, SIZE // 2):
            row = []
            # individual entries in the row.
            for j in range(SIZE, SIZE // 2, -1):

                row = row + [j-2 - i]
            # print(row)
            row += copy.deepcopy(row[::-1])
            # print(row)
            grid.append(row)
        grid += copy.deepcopy(grid[::-1])
    return grid


def  find_neighbouring_cells(pos):
    """
    Returns the position of the neighbouring cells in a list.
    :param Grid: It is the maze internal representation with flood values
    :param pos: (x, y) with x denoting the row number we are in and y would be the column number in the grid
    :return: a list of neighboring cells with their position and flood value.
    """
    global grid

    nbr_cells =[]
    x, y = pos
    if x != 0:
        N_pos = (x - 1, y)
        nbr_cells.append([N_pos, grid[N_pos[0]][N_pos[1]], N])
    if y != SIZE - 1:
        E_pos = (x, y + 1)

        nbr_cells.append([E_pos, grid[E_pos[0]][E_pos[1]], E])
    if x != SIZE - 1:
        S_pos = (x + 1, y)
        nbr_cells.append([S_pos, grid[S_pos[0]][S_pos[1]], S])
    if y != 0:
        W_pos = (x, y - 1)
        nbr_cells.append([W_pos, grid[W_pos[0]][W_pos[1]], W])


    return nbr_cells

def sort_nbr_cells(nbr_cells):
    nbr_cells.sort(key = lambda x: x[1])


def check_if_blocked(cell):
    global MOUSE_DIR
    if MOUSE_DIR == cell[2]:

        log("Robot is facing cell")
        log(str(MOUSE_DIR))
        if wallFront():
            log("before crash")
            return True

        else:
            return False

    else:
        log("Robot is not facing cell")
        log(str(MOUSE_DIR))
        while MOUSE_DIR != cell[2]:
            turnRight()
            MOUSE_DIR = (MOUSE_DIR+1)%4

        if wallFront():
            return True
        else:
            return False

def pretty_print():
    stringout = ""
    for row in grid:
        for cell in row:
            stringout+= "{:^4}".format(cell)
        stringout+= "\n"
    return stringout

def goto(target):
    global MOUSE_DIR
    global pos
    if MOUSE_DIR == target[2]:
        moveForward()
    if MOUSE_DIR != target[2]:
        while MOUSE_DIR != target[2]:
            turnRight()
            MOUSE_DIR = (MOUSE_DIR + 1) % 4
        moveForward()
    pos = target[0]


def rec_move(curr_pos):
    global MOUSE_DIR
    global grid
    global pos
    global prev_cell
    pos = curr_pos[0]

    log("Running...")
    setColor(0, 0, "G")
    setText(0, 0, "abc")

    #base case
    if grid[curr_pos[0][0]][curr_pos[0][1]] == 0:
        return "YAY"
    #Recursive case
    else:
        nbr_cells = find_neighbouring_cells(pos)
        log("line 138" + str(nbr_cells))
        sort_nbr_cells(nbr_cells)
        log("line 141 sorted nbr cells:" + str(nbr_cells))
        lowest_flood_val_cell = nbr_cells[0]

        i = 0
        while check_if_blocked(lowest_flood_val_cell) and i < len(nbr_cells)-1:
            i = i+1
            lowest_flood_val_cell = nbr_cells[i]
        log(str(lowest_flood_val_cell))


        if prev_cell != [] and i<len(nbr_cells) and grid[lowest_flood_val_cell[0][0]][lowest_flood_val_cell[0][1]] == grid[nbr_cells[i][0][0]][nbr_cells[i][0][1]]:
            if lowest_flood_val_cell[0] == prev_cell[0] and check_if_blocked(nbr_cells[i]):
                lowest_flood_val_cell = nbr_cells[i]

        if grid[lowest_flood_val_cell[0][0]][lowest_flood_val_cell[0][1]] > grid[curr_pos[0][0]][curr_pos[0][1]]: #or check_if_blocked(lowest_flood_val_cell):
            # log(str(lowest_flood_val_cell))
            grid[curr_pos[0][0]][curr_pos[0][1]] += 2
            return curr_pos
        else:
            if grid[lowest_flood_val_cell[0][0]][lowest_flood_val_cell[0][1]] == grid[curr_pos[0][0]][curr_pos[0][1]] :
                grid[curr_pos[0][0]][curr_pos[0][1]] += 1
            prev_cell = [pos, grid[curr_pos[0][0]][curr_pos[0][1]], (lowest_flood_val_cell[2] - 2)% 4]
            goto(lowest_flood_val_cell)
            return lowest_flood_val_cell



def start_here(): # CHANGE
    result = rec_move([(15,0), grid[15][0], N])
    while result != "YAY":
        result = rec_move(result)


if __name__ == "__main__":
    createGrid()
    start_here()
