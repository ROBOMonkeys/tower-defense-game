from pygame import mouse, time
from ui.interfaces import Drawable, Clickable
from ui.enums import TILE_H, TILE_W
from util.util import map_cover_up, screen_cover_up, \
    get_map_size, parse_spritesheet
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
        self.tick = 0

    def get_next_frame(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        return self.frames[self.frame]

    def animate(self, ticks):
        self.tick += 1
        if self.tick >= ticks:
            self.tick = 0
            self.srf = self.get_next_frame()


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


class Robot(Animated, Moveable):

    MOVING = 0
    ATTACKING = 1
    DYING = 3

    def __init__(self, frames, spd):
        Animated.__init__(self, frames)
        self.damage = 0
        self.hp = 0
        self.speed = spd
        self.srf = self.frames[0]
        self.height = self.srf.get_height()
        self.width = self.srf.get_width()
        self.location = [0, 0]
        self.state = Robot.MOVING

    def set_location(self, loc):
        self.location = loc

    def update(self):
        self.srf = self.get_next_frame()

    def die(self):
        del self


class Tower(Animated, Intelligent, Clickable):
    """
    Class that gathers together the base functionality for a tower

    Statics:
     PLACEMENT = the mode when the tower is being placed
     CHECKING  = the mode when the tower is checking if it can be placed
     IDLE      = the mode when the tower is placed and waiting
     ATTACKING = the mode when the tower is attacking

    Vars:
     frames = a list of Surfaces to be used for animation
    """
    PLACEMENT = 0
    CHECKING = 1
    IDLE = 2
    ATTACKING = 3

    WOOD = 0
    IRON = 1
    GOLD = 2
    PLATINUM = 3
    PLUTONIUM = 4

    def __init__(self, frames, cost, hp, dmg, name):
        Animated.__init__(self, frames)
        self.state = Tower.PLACEMENT
        self.location = (0, 0)
        self.srf = self.frames[0]
        self.width = self.srf.get_width()
        self.height = self.srf.get_height()
        self.name = name

        self.hp = hp
        self.damage = dmg
        self.cost = cost
        self.level = Tower.WOOD

        self.update()

    def update(self):
        """
        function to be run every tick to keep the object up to date
        """
        pos = mouse.get_pos()
        mp_sz = get_map_size()
        x = int(pos[0] / TILE_W)
        y = int(pos[1] / TILE_H)
        btns = mouse.get_pressed()
        if btns[0] and pos[0] < mp_sz[0] and pos[1] < mp_sz[1] \
           and self.state == Tower.PLACEMENT:
            self.state = Tower.CHECKING
        screen_cover_up(self.location, (self.width,
                                        self.height))
        if btns[2] and self.state == Tower.PLACEMENT:
            util.enums.SPRITES[0].pop()
            util.enums.MONEY += self.cost
            return
        elif btns[2]:
            self.click()
        if self.state == Tower.PLACEMENT:
            self.location = pos
        elif self.state == Tower.CHECKING:
            if pos[0] < mp_sz[0] and pos[1] < mp_sz[1]:
                if self.check_under(x, y):
                    self.location = (x * TILE_W, y * TILE_H)
                    self.add_to_bg()
                    self.state = Tower.IDLE
                else:
                    self.state = Tower.PLACEMENT
        elif self.state == Tower.IDLE:
            if self.frame != 0:
                self.frame = 0
        elif self.state == Tower.ATTACKING:
            map_cover_up(self.location, (self.width, self.height))
            self.animate(50)
        self.srf = self.frames[self.frame]
        self.draw(util.enums.SCREEN)

    def set_state(self, s):
        self.state = s

    def click(self):
        time.delay(100)
        if self.isOver():
            if self.state == 3:
                self.state = 2
            elif self.state == 2:
                self.state = 3

    def check_under(self, x, y):
        """
        function that checks if the tile under the tower is good for placement

        Vars:
         x = the x position of the tower
         y = the y position of the tower

        Returns:
         True or False
        """
        try:
            if (util.enums.MAP_GRID[y + 2][x] == 1 or
                util.enums.MAP_GRID[y - 2][x] == 1 or
                util.enums.MAP_GRID[y][x + 2] == 1 or
                util.enums.MAP_GRID[y][x - 2] == 1) and \
               (util.enums.MAP_GRID[y + 1][x] != 1 and
                util.enums.MAP_GRID[y - 1][x] != 1 and
                util.enums.MAP_GRID[y][x + 1] != 1 and
                util.enums.MAP_GRID[y][x - 1] != 1) and \
                util.enums.MAP_GRID[y][x] != 1 and \
               util.enums.MAP_GRID[y][x] != 2:
                util.enums.MAP_GRID[y][x] = 2
                return True
            return False
        except:
            try:
                if (util.enums.MAP_GRID[y][x + 2] == 1 or
                    util.enums.MAP_GRID[y][x - 2] == 1) and \
                    util.enums.MAP_GRID[y][x] != 1 and \
                   util.enums.MAP_GRID[y][x] != 2:
                    util.enums.MAP_GRID[y][x] = 2
                    return True
                return False
            except:
                try:
                    if (util.enums.MAP_GRID[y - 2][x] == 1) and \
                        util.enums.MAP_GRID[y][x] != 1 and \
                       util.enums.MAP_GRID[y][x] != 2:
                        util.enums.MAP_GRID[y][x] = 2
                        return True
                    return False
                except:
                    return False

    def add_to_bg(self):
        x, y = self.location
        util.enums.BG.blit(self.srf,
                           self.location)

    def upgrade(self):
        if self.level < Tower.PLUTONIUM:
            self.state = Tower.IDLE
            self.level += 1
            frs = parse_spritesheet(util.enums.RES +
                                    "spritesheets/" +
                                    str(self.name) + "_" +
                                    str(self.level) +
                                    "_ss.png")
            for f in range(len(frs)):
                self.frames[f] = frs[f]
            self.frame = 0
            self.srf = self.frames[self.frame]
            self.add_to_bg()


class Group():
    def __init__(self, obj=None):
        self.ctr = 0
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

    def pop(self):
        self.list.pop()

    def __iter__(self):
        return self

    def next(self):
        try:
            res = self.list[self.ctr]
        except IndexError:
            raise StopIteration
        self.ctr += 1
        return res
