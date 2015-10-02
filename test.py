import util.enums as enums
from sprites.sprites import ProjectileTower
from pygame import image


def test():
    print('okay')


def print_grid(pos=None):
    if pos is not None:
        for i in range(len(enums.MAP_GRID)):
            for j in range(len(enums.MAP_GRID[i])):
                if i == pos[0] and j == pos[1]:
                    print 'X',
                else:
                    print enums.MAP_GRID[i][j],
            print 
    for i in range(len(enums.MAP_GRID)):
        for j in range(len(enums.MAP_GRID[i])):
            print enums.MAP_GRID[i][j],
        print


def print_grid_len():
    print len(enums.MAP_GRID)
    prin_str = ""
    for i in range(len(enums.MAP_GRID)):
        num_ones = 0
        for j in range(len(enums.MAP_GRID[i])):
            if enums.MAP_GRID[i][j]:
                num_ones += 1
        prin_str += str(i) + ":" + str(num_ones) + ", "
    print prin_str


def start_game():
    print('game started')


def open_options():
    print('options opened')


def make_new_proj_tower():
    enums.SPRITES[0].add(ProjectileTower())
