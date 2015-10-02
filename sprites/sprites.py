from pygame import image
from interfaces import Robot, Intelligent, Tower
import util.enums


class AutoRobot(Robot, Intelligent):
    def __init__(self, frames):
        Robot.__init__(self, frames)


class ProjectileTower(Tower):
    def __init__(self):
        proj_img = image.load(util.enums.RES +
                              "towers/proj_wood_ig.png").convert_alpha()
        Tower.__init__(self, proj_img, 10, 15, 5)
