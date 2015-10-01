import util.enums as enums


def test():
    print('okay')


def print_grid():
    for i in range(len(enums.MAP_GRID)):
        print enums.MAP_GRID[i]


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
