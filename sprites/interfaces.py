from ui.interfaces import Drawable
from util.util import cover_up
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

    def next_frame(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        return self.frames[self.frame]


class Moveable(Drawable):
    def move_up(self):
        moved = self.calc_movement()
        cover_up(self.location, (self.height, self.width))
        self.location[1] -= int(moved[1])
        self.draw(util.enums.SCREEN)

    def move_down(self):
        moved = self.calc_movement()
        cover_up(self.location, (self.height, self.width))
        self.location[1] += int(moved[1])
        self.draw(util.enums.SCREEN)

    def move_left(self):
        moved = self.calc_movement()
        cover_up(self.location, (self.height, self.width))
        self.location[0] -= int(moved[0])
        self.draw(util.enums.SCREEN)

    def move_right(self):
        moved = self.calc_movement()
        cover_up(self.location, (self.height, self.width))
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


class Creature(Animated, Moveable, Intelligent):
    def __init__(self, frames):
        Animated.__init__(self, frames)
        self.damage = 0
        self.hp = 0
        self.speed = 0
        self.srf = self.frames[0]
        self.height = self.srf.get_height()
        self.width = self.srf.get_width()
        self.location = [0, 0]

    def set_location(self, loc):
        if type(loc) == tuple:
            x, y = loc
            loc = (x, y)
        self.location = loc
