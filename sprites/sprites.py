from pygame import image
from interfaces import Robot, Intelligent, Tower
from util.util import parse_spritesheet
import util.enums


class AutoRobot(Robot, Intelligent):
    def __init__(self, frames):
        Robot.__init__(self, frames)


class ProjectileTower(Tower):
    def __init__(self):
        Tower.__init__(self, parse_spritesheet(util.enums.RES +
                                               "spritesheets/" +
                                               "proj_0_ss.png"),
                       10, 15, 5, "proj")
