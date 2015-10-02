from pygame import mouse
from ui.interfaces import Drawable
from ui.enums import TILE_H, TILE_W
from util.util import map_cover_up, screen_cover_up, \
    get_map_size
import util.enums


class Intelligent():
    pass


class Animated():
    def __init__(self, frames):
        self.frames = []
        if type(frames) == tuple:
            for frame in frames:
                self.frames.append(frame)
        else:
            self.frames.append(frames)
        self.frame = 0

    def get_next_frame(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        return self.frames[self.frame]


class Moveable(Drawable):
    def move_up(self):
        moved = self.calc_movement()
        map_cover_up(self.location, (self.width, self.height))
        self.location[1] -= int(moved[1])
        self.draw(util.enums.SCREEN)

    def move_down(self):
        moved = self.calc_movement()
        map_cover_up(self.location, (self.width, self.height))
        self.location[1] += int(moved[1])
        self.draw(util.enums.SCREEN)

    def move_left(self):
        moved = self.calc_movement()
        map_cover_up(self.location, (self.width, self.height))
        self.location[0] -= int(moved[0])
        self.draw(util.enums.SCREEN)

    def move_right(self):
        moved = self.calc_movement()
        map_cover_up(self.location, (self.width, self.height))
        self.location[0] += int(moved[0])
        self.draw(util.enums.SCREEN)

    def calc_movement(self):
        moved_h = self.height * self.speed
        moved_w = self.width * self.speed
        return (moved_h, moved_w)

    def moved_coord(self, loc, mvmnt):
        x = loc[0] - mvmnt[0]
        y = loc[1] - mvmnt[1]
        return (x, y)


class Creature(Animated, Moveable):
    def __init__(self, frames, spd):
        Animated.__init__(self, frames)
        self.damage = 0
        self.hp = 0
        self.speed = spd
        self.srf = self.frames[0]
        self.height = self.srf.get_height()
        self.width = self.srf.get_width()
        self.location = [0, 0]
        self.state = 0

    def set_location(self, loc):
        if type(loc) == tuple:
            x, y = loc
            loc = (x, y)
        self.location = loc

    def update(self):
        self.srf = self.get_next_frame()

    def die(self):
        del self


class Tower(Animated, Intelligent, Drawable):
    def __init__(self, frames):
        Animated.__init__(self, frames)
        self.state = 0
        self.location = (0, 0)
        self.srf = self.frames[0]
        self.width = self.srf.get_width()
        self.height = self.srf.get_height()
        self.update()

    def update(self):
        pos = mouse.get_pos()
        mp_sz = get_map_size()
        if mouse.get_pressed()[0] and pos[0] < mp_sz[0] and pos[1] < mp_sz[1] \
           and self.state < 2:
            self.clicked()
        screen_cover_up(self.location, (self.width,
                                        self.height))
        if self.state == 0:
            self.location = pos
        elif self.state == 1:
            if pos[0] < mp_sz[0] and pos[1] < mp_sz[1]:
                if self.check_under(pos):
                    x = int(pos[0] / TILE_W)
                    y = int(pos[1] / TILE_H)
                    self.location = (x * TILE_W, y * TILE_H)
                    self.state += 1
        elif self.state == 2:
            pass
        self.draw(util.enums.SCREEN)

    def clicked(self):
        self.state += 1

    def check_under(self, pos):
        x = int(pos[0] / TILE_W)
        y = int(pos[1] / TILE_H)
        print_grid((y, x))
        print
        if util.enums.MAP_GRID[y + 2][x] == 1 or \
           util.enums.MAP_GRID[y - 2][x] == 1 or \
           util.enums.MAP_GRID[y][x + 2] == 1 or \
           util.enums.MAP_GRID[y][x - 2] == 1:
            return True
        return False


class Group():
    def __init__(self, obj=None):
        if obj is None:
            self.list = []
        elif type(obj) != tuple:
            self.list.append(obj)
        else:
            for o in obj:
                self.list.append(o)

    def update(self):
        for obj in self.list:
            obj.update()

    def add(self, obj):
        self.list.append(obj)

def print_grid(pos=None):
    if pos is not None:
        for i in range(len(util.enums.MAP_GRID)):
            for j in range(len(util.enums.MAP_GRID[i])):
                if i == pos[0] and j == pos[1]:
                    print 'X',
                else:
                    print util.enums.MAP_GRID[i][j],
            print
    else:
        for i in range(len(util.enums.MAP_GRID)):
            for j in range(len(util.enums.MAP_GRID[i])):
                print util.enums.MAP_GRID[i][j],
            print
